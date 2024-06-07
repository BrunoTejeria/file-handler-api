import dotenv
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
import os
import re

dotenv.load_dotenv()
vars = {
    "FILES_FOLDER": os.getenv("FILES_FOLDER")
}
print(vars["FILES_FOLDER"])

app = FastAPI()

@app.get("/")
def test(request: Request, response: Response):
    return HTMLResponse("<h1>File Handler API</h1>", 200)

@app.get("/file")
def file(request: Request, response: Response, file: str):
    if re.search(r"[./\\]", file):
        return JSONResponse(status_code=400, content=jsonable_encoder({"error": "Nombre no valido"}))
    with open(f"./uploads/{file}.txt", "r") as f:
        return JSONResponse(status_code=200, content={"error": None, "message": "Archivo leído exitosamente","data": f.read()})

@app.get("/fileBin")
def file(request: Request, response: Response, file: str):
    if re.search(r"[./\\]", file):
        return JSONResponse(status_code=400, content=jsonable_encoder({"error": "Nombre no valido"}))
    with open(f"./uploads/{file}.txt", "rb") as f:
        return JSONResponse(status_code=200, content={"error": None, "message": "Archivo leído exitosamente","data": str(f.read())})

