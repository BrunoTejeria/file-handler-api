from fastapi import FastAPI

from .routers.download import router as DownloadRouter
from .routers.upload import router as UploadRouter
from .routers.delete import router as DeleteRouter
from .routers.others import router as OthersRouter

from .middlewares.log_request import LogRequestsMiddleware


app = FastAPI()
app.add_middleware(LogRequestsMiddleware)

app.include_router(DownloadRouter, tags=["download"])
app.include_router(UploadRouter, tags=["upload"])
app.include_router(DeleteRouter, tags=["delete"])
app.include_router(OthersRouter, tags=["others"])









