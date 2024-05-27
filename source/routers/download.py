from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from ..services.download import Download as DownloadService

router = APIRouter()

@router.get("/download")
def download(request: Request, response: Response, file: str):
    """
    Endpoint to download a file in a standard format.
    
    Parameters:
    - request: Request object.
    - response: Response object.
    - file: str, the name or path of the file to be downloaded.
    
    Returns:
    - A response from the DownloadService with the requested file.
    """
    return DownloadService.download(file)

@router.get("/download-bin")
def download_bin(request: Request, response: Response, file: str):
    """
    Endpoint to download a file in binary format.
    
    Parameters:
    - request: Request object.
    - response: Response object.
    - file: str, the name or path of the file to be downloaded in binary format.
    
    Returns:
    - A binary response from the DownloadService with the requested file.
    """
    return DownloadService.download_bin(file)