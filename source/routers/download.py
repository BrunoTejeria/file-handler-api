from fastapi import APIRouter, Request, Response

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

@router.get("/files-list")
def get_files_list():
    """
    Endpoint to retrieve a list of all files stored in the uploads database.

    Returns:
    - The response from the DownloadService.get_files_list() method, which is a JSON
      response containing a list of file names and a success message, or an error message
      if no files are found.
    """
    return DownloadService.get_files_list()