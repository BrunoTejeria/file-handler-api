from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi import File as FileType, UploadFile
import os
import re

from .utils.responses import Responses
from .middlewares.log_request import LogRequestsMiddleware
from .database import Session
from .models.files import Files as FilesModel



app = FastAPI()
app.add_middleware(LogRequestsMiddleware)

@app.get("/")
def test(request: Request, response: Response):
    return Responses.html(status=200, data="<h1>File Handler</h1>")

@app.get("/download")
def file(request: Request, response: Response, file: str):
    if re.search(r"[./\\]", file):
        return JSONResponse(status_code=400, content=jsonable_encoder({"error": "Nombre no valido"}))
    with open(f"./uploads/{file}.txt", "r") as f:

        return Responses.json(status=200, data=f.read(), message="Archivo leído exitosamente")

@app.get("/download-bin")
def file(request: Request, response: Response, file: str):
    if re.search(r"[./\\]", file):
        return Responses.error(err=True, status=400, message="Nombre no valido")
    with open(f"./uploads/{file}.txt", "rb") as f:
        return Responses.json(status=200, data=str(f.read()), message="Archivo leído exitosamente")

@app.post("/upload")
async def upload(request: Request, response: Response, file: UploadFile = FileType(...)):
    if not file.filename.endswith('.txt'):
        return Responses.error(err=True, status=400, message="El archivo no tiene la extensión .txt")

    contents = {
        # "bin": asyncio.run(file.read()),
        # "str": asyncio.run(file.read()).decode("utf-8")
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

@app.delete("/delete")
def delete(request: Request, response: Response, file: str):
    if re.search(r"[./\\]", file):
        return Responses.error(err=True, status=400, message="Nombre no valido")
    os.remove(f"./uploads/{file}.txt")
    return Responses.json(status=200, data=None, message="Archivo eliminado con éxito")

