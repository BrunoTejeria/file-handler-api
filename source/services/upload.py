from fastapi import Request, File as FileType, UploadFile
from typing import Union

from ..utils.responses import Responses
from ..libs.database import Session
from ..models.files import Files as FilesModel
from ..schemas.data_validators import Validators
from ..utils.env import __env__

class Upload:
    @staticmethod
    async def upload(request: Request, name: str, description: str = "", tags: list = [], file: UploadFile = FileType(...)) -> Union[Responses.json, Responses.error]:
        """
        Asynchronously uploads a .txt file, validates it, and saves its content to the database and filesystem.

        This method performs several key operations:
        - Validates that the uploaded file has a .txt extension.
        - Reads the content of the file and decodes it from binary to a string.
        - Checks if the file is empty.
        - Saves the file's metadata and content to the database.
        - Returns a JSON response indicating the outcome of the operation.

        Parameters:
        - request (Request): The request object, used to access request-specific data like the client's host.
        - name (str): The file's name.
        - description (str): The file's description.
        - tags (list, optional): The file's tags. Defaults to an empty list.
        - file (UploadFile, optional): The file to be uploaded. Defaults to FileType(...), which requires a file to be provided.

        Returns:
        - Union[Responses.json, Responses.error]: A JSON response indicating the success or failure of the upload operation.
          If the file is not a .txt file or is empty, an error response is returned. Otherwise, a success message and the
          content of the uploaded file are returned.

        Raises:
        - HTTPException: If the file extension is not .txt or the file is empty, an HTTPException with status code 400 is raised.

        Note:
        - The file's binary content is decoded to a string before being stored and returned in the response.
        - The method assumes that the file has a '.txt' extension and validates it accordingly.
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

        # Check if the file size is within the allowed limit
        if Validators.file.size(__env__["files"]["max_size"], contents["bin"]):
            return Responses.error(err=True, status=400, message="El archivo es demasiado grande. Tamaño máximo: 64 MB")

        # Save the file's metadata and content to the database
        with Session() as db:
            db.add(FilesModel(name=file.filename, created_by=request.client.host, data=contents["bin"]))
            db.commit()
            db.close()

        # Return a success response with the file's content
        return Responses.json(status=200, data=contents["str"][0:1024]+"...", message="Archivo subido con éxito")