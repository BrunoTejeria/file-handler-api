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
