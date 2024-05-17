from fastapi import FastAPI, Request, Response
import os
import re

from .routers.download import router as DownloadRouter
from .routers.upload import router as UploadRouter
from .routers.delete import router as DeleteRouter
from .routers.others import router as OthersRouter

from .utils.responses import Responses
from .middlewares.log_request import LogRequestsMiddleware


app = FastAPI()
app.add_middleware(LogRequestsMiddleware)

app.include_router(DownloadRouter)
app.include_router(UploadRouter)
app.include_router(DeleteRouter)
app.include_router(OthersRouter)

@app.get("/")
def test(request: Request, response: Response):
    return Responses.html(status=200, data="<h1>File Handler</h1>")







