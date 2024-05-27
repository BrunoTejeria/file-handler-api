from fastapi import Request, File as FileType, UploadFile
from typing import Union

from ..utils.responses import Responses
from ..libs.database import Session
from ..models.files import Files as FilesModel
from ..schemas.data_validators import Validators

class Upload:
    @staticmethod
    async def upload(request: Request, file: UploadFile = FileType(...)) -> Union[Responses.json, Responses.error]:
        """
        Asynchronously uploads a .txt file and saves its content to the database and filesystem.

        Validates the file extension to ensure it is a .txt file and checks that the file is not empty.
        The file's metadata and content are stored in the database, and the file itself is saved in the
        './uploads' directory.

        Parameters:
        - request (Request): The request object.
        - file (UploadFile, optional): The file to be uploaded. Defaults to FileType(...) which requires a file.

        Returns:
        - A JSON response indicating the outcome of the upload operation. If the file is not a .txt file,
          or if it is empty, an error response is returned. Otherwise, a success message is returned along
          with the content of the uploaded file.

        Note:
        - This method assumes that the file has a '.txt' extension and validates it accordingly.
        - The file's binary content is decoded to a string before being stored and returned in the response.
        """
        # Validate the file extension
        if Validators.file.txt(file.filename):
            return Responses.error(err=True, status=400, message="Solo se aceptan archivos .txt")

        # Read the file's content
        contents = {
            "bin": await file.read(),
        }
        # Decode the binary content to a string
        contents["str"] = contents["bin"].decode("utf-8")

        # Check if the file is empty
        if len(contents["str"]) < 1:
            return Responses.error(err=True, status=400, message="El archivo está vacío")

        # Save the file's metadata to the database
        db = Session()
        db.add(FilesModel(name=file.filename, created_by=request.client.host))
        db.commit()
        db.close()

        # Save the file to the filesystem
        with open(f"./uploads/{file.filename}", "wb") as f:
            f.write(contents["bin"])

        # Return a success response with the file's content
        return Responses.json(status=200, data=contents["str"], message="Archivo subido con éxito")
