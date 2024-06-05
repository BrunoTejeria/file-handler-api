from fastapi.responses import JSONResponse
from typing import Union
from base64 import b64encode

from ..utils.responses import Responses
from ..schemas.data_validators import Validators
from ..libs.database import Session
from ..models.files import Files as FilesModel

class Download:
    @staticmethod
    def download(file: str) -> Union[Responses.json, Responses.error]:
        """
         Downloads a binary file from the server's uploads db.

        Validates the file name to prevent directory traversal attacks. If the file name is valid,
        it reads the binary content of the file in db and returns it as a string in the response.

        Parameters:
        - file (str): The name of the binary file to be downloaded.

        Returns:
        - A JSON response with the file's content if successful, or an error message if the file name is invalid.
        """
        if Validators.file.basic(file):
            return Responses.error(err=True, status=400, message="Nombre no valido")
        file = file +".txt"

        with Session() as db:
            query = db.query(FilesModel).filter(FilesModel.name == file).first()
            db.close()
            if query:
                return Responses.json(status=200, data=str(query.data), message="Archivo leído exitosamente")
            else:
                return Responses.error(err=True, status=404, message="Archivo no encontrado")

    @staticmethod
    def download_bin(file: str) -> Union[Responses.json, Responses.error]:
        """
        Downloads a binary file from the server's uploads db.

        Validates the file name to prevent directory traversal attacks. If the file name is valid,
        it reads the binary content of the file in db and returns it.

        Parameters:
        - file (str): The name of the binary file to be downloaded.

        Returns:
        - A JSON response with the binary file's content (as an base64) if successful, or an error message if the file name is invalid.
        """
        if Validators.file.basic(file):
            return Responses.error(err=True, status=400, message="Nombre no valido")
        file = file +".txt"

        with Session() as db:
            query = db.query(FilesModel).filter(FilesModel.name == file).first()
            db.close()
            if query:
                return Responses.json(status=200, data=b64encode(query.data).decode('ascii'), message="Archivo leído exitosamente")
            else:
                return Responses.error(err=True, status=404, message="Archivo no encontrado")
    
    @staticmethod
    def get_files_list() -> Union[Responses.json, Responses.error]:
        """
        Retrieves a list of all file names stored in the uploads database and returns them in a JSON response.

        This method queries the database for all entries in the FilesModel, specifically fetching the names of the files.
        It then formats these names into a list and returns them as part of a successful JSON response. If no files are found,
        it returns an error response indicating that no files were found.

        Returns:
        - Responses.json: If files are found, returns a JSON response with a status code of 200 and a list of file names.
        - Responses.error: If no files are found, returns a JSON error response with a status code of 404.
        """
        with Session() as db:
            query = db.query(FilesModel.name).all()
            db.close()
            if query:
                return Responses.json(status=200, data=[name for name, in query], message="Nombre de archivos encontrados con éxito.")
            else:
                return Responses.error(err=True, status=404, message="Archivos no encontrados")
