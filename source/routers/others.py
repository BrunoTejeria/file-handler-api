from fastapi import APIRouter, Request, Response

# Import the Others service from the services module.
from ..services.others import Others as OthersService

router = APIRouter()

@router.get("/", tags=["others"])
def docs(request: Request, response: Response):
    """
    Endpoint GET requests at the root path, returning documentation or other data from the OthersService.

    Parameters:
    - request (Request): The request object.
    - response (Response): The response object.

    Returns:
    - The result of calling the `docs` method on the OthersService.
    """
    return OthersService.docs()