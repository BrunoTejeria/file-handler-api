from fastapi import APIRouter, Request, Response
from fastapi import File as FileType, UploadFile

from ..utils.responses import Responses
from ..libs.database import Session
from ..models.files import Files as FilesModel
from ..schemas.data_validators import Validators


router = APIRouter()


@router.post("/upload")
async def upload(request: Request, response: Response, file: UploadFile = FileType(...)):
    if Validators.file.txt(file.filename):
        return Responses.error(err=True, status=400, message="Solo se aceptan archivos .txt")

    contents = {
        "bin": await file.read(),
    }
    contents["str"] = contents["bin"].decode("utf-8")
    if len(contents["str"]) < 1:
        return Responses.error(err=True, status=400, message="El archivo está vacío")

    db = Session()
    db.add(FilesModel(name=file.filename, created_by=request.client.host))
    db.commit()
    db.close()

    with open(f"./uploads/{file.filename}", "wb") as f:
        f.write(contents["bin"])

    return Responses.json(status=200, data=contents["str"], message="Archivo subido con éxito")