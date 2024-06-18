from fastapi import APIRouter, Request, Response
from fastapi import File as FileType, UploadFile

from ..services.upload import Upload as UploadService
from ..schemas.requests.upload import Schemas

router = APIRouter()

@router.post("/upload")
async def upload(request: Request, response: Response, query: Schemas.Upload, file: UploadFile = FileType(...)):
    """
    Endpoint to upload a file.

    This endpoint accepts a file upload along with the request and response objects,
    and delegates the actual upload process to the UploadService.

    Parameters:
    - request (Request): The request object.
    - response (Response): The response object.
    - query (Schemas.Upload, optional): The query parameters.
    - file (UploadFile): The file to be uploaded. Defaults to an empty file placeholder.

    Returns:
    - The result of the upload process, as returned by the UploadService's upload method.
    """
    return await UploadService.upload(request, query.name, query.description, query.tags, file)