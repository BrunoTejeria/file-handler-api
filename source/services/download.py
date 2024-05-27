from fastapi.responses import JSONResponse
from typing import Union

from ..utils.responses import Responses
from ..schemas.data_validators import Validators

class Download:
    @staticmethod
    def download(file: str) -> Union[Responses.json, Responses.error]:
        """
        Downloads a text file from the server's uploads directory.

        Validates the file name to prevent directory traversal attacks. If the file name is valid,
        it reads the file's content and returns it in the response.

        Parameters:
        - file (str): The name of the file to be downloaded.

        Returns:
        - A JSON response with the file's content if successful, or an error message if the file name is invalid.
        """
        if Validators.file.basic(file):
            return Responses.error(err=True, status=400, message="Nombre no valido")
        with open(f"./uploads/{file}.txt", "r") as f:
            return Responses.json(status=200, data=f.read(), message="Archivo leído exitosamente")

    @staticmethod
    def download_bin(file: str) -> Union[Responses.json, Responses.error]:
        """
        Downloads a binary file from the server's uploads directory.

        Validates the file name to prevent directory traversal attacks. If the file name is valid,
        it reads the binary content of the file and returns it as a string in the response.

        Parameters:
        - file (str): The name of the binary file to be downloaded.

        Returns:
        - A JSON response with the binary file's content (as a string) if successful, or an error message if the file name is invalid.
        """
        if Validators.file.basic(file):
            return Responses.error(err=True, status=400, message="Nombre no valido")
        with open(f"./uploads/{file}.txt", "rb") as f:
            return Responses.json(status=200, data=str(f.read()), message="Archivo leído exitosamente")