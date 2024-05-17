from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import os
import re

from ..utils.responses import Responses
from ..schemas.data_validators import Validators


router = APIRouter()


@router.delete("/delete")
def delete(request: Request, response: Response, file: str):
    if re.search(r"[./\\]", file):
        return Responses.error(err=True, status=400, message="Nombre no valido")
    os.remove(f"./uploads/{file}.txt")
    return Responses.json(status=200, data=None, message="Archivo eliminado con éxito")