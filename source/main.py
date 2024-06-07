import dotenv
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi import File as FileType, UploadFile
import os
import re
import asyncio

from .utils.responses import Responses
from .middlewares.log_request import LogRequestsMiddleware


dotenv.load_dotenv()
vars = {
    "FILES_FOLDER": os.getenv("FILES_FOLDER")
}

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
def upload(request: Request, response: Response, file: UploadFile = FileType(...)):
    if not file.filename.endswith('.txt'):
        return Responses.error(err=True, status=400, message="El archivo no tiene la extensión .txt")

    contents = {
        "bin": asyncio.run(file.read()),
        "str": asyncio.run(file.read()).decode("utf-8")
    }

    if len(contents["str"]) < 1:
        return Responses.error(err=True, status=400, message="El archivo está vacío")

    with open(f"./uploads/{file.filename}", "wb") as f:
        f.write(contents["bin"])

    return Responses.json(status=200, data=contents["str"], message="Archivo subido con éxito")

