from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from ..utils.responses import Responses
from ..schemas.data_validators import Validators


router = APIRouter()

@router.get("/download")
def file(request: Request, response: Response, file: str):
    if Validators.file.basic(file):
        return JSONResponse(status_code=400, content=jsonable_encoder({"error": "Nombre no valido"}))
    with open(f"./uploads/{file}.txt", "r") as f:
        return Responses.json(status=200, data=f.read(), message="Archivo leído exitosamente")

@router.get("/download-bin")
def file(request: Request, response: Response, file: str):
    print(Validators.file.basic(file))
    if Validators.file.basic(file):
        return Responses.error(err=True, status=400, message="Nombre no valido")
    with open(f"./uploads/{file}.txt", "rb") as f:
        return Responses.json(status=200, data=str(f.read()), message="Archivo leído exitosamente")

