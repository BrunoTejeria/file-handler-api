from fastapi import APIRouter, Request, Response

from ..services.delete import Delete as DeleteService

router = APIRouter()

@router.delete("/delete")
def delete(request: Request, response: Response, file: str):
    """
    Endpoint to delete a specified file.

    Parameters:
    - request (Request): The request object.
    - response (Response): The response object.
    - file (str): The name of the file to be deleted.

    Returns:
    - The result of the delete operation from the DeleteService.
    """
    return DeleteService.delete(file)