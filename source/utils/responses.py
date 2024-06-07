from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder

class Responses:
    """
    A class to handle different types of responses in a FastAPI application.
    """

    @staticmethod
    def json(err: bool | None = None, status: int = 200, data: str | int | dict | list = "", message: str | None = None) -> JSONResponse:
        """
        Returns a JSON response.

        Parameters:
        - err (bool | None): Indicates if there is an error. Default is None.
        - status (int): The HTTP status code. Default is 200.
        - data (str | int | dict | list): The data to be included in the response. Default is an empty string.
        - message (str | None): A message to be included in the response. Default is None.

        Returns:
        - JSONResponse: A JSON response with the specified status code, error, message, and data.
        """
        return JSONResponse(status_code=status, content={"error": err, "message": message, "data": data})

    @staticmethod
    def html(err: bool | None = None, status: int = 200, data: str = "<></>", message: str | None = None) -> HTMLResponse:
        """
        Returns an HTML response.

        Parameters:
        - err (bool | None): Indicates if there is an error. Default is None.
        - status (int): The HTTP status code. Default is 200.
        - data (str): The HTML content to be included in the response. Default is an empty HTML tag.
        - message (str | None): A message to be included in the response. Default is None.

        Returns:
        - HTMLResponse: An HTML response with the specified status code and content.
        - JSONResponse: A JSON response with the specified status code, error and message.
        """
        if err:
            return JSONResponse(status_code=status, content=jsonable_encoder({"error": err, "message": message}))
        return HTMLResponse(content=data, status_code=200)

    @staticmethod
    def file(err: bool | None = None, status: int = 200, file: bytes = b"", message: str | None = None) -> FileResponse:
        """
        Returns a file response.

        Parameters:
        - err (bool | None): Indicates if there is an error. Default is None.
        - status (int): The HTTP status code. Default is 200.
        - file (bytes): The file content to be included in the response. Default is an empty byte string.
        - message (str | None): A message to be included in the response. Default is None.

        Returns:
        - FileResponse: A file response with the specified status code and content.
        - JSONResponse: A JSON response with the specified status code, error and message.
        """
        if err:
            return JSONResponse(status_code=status, content=jsonable_encoder({"error": err, "message": message}))
        return FileResponse(content=file, status_code=200)