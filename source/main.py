from fastapi import FastAPI

from .routers.download import router as DownloadRouter
from .routers.upload import router as UploadRouter
from .routers.delete import router as DeleteRouter
from .routers.others import router as OthersRouter

from .middlewares.log_request import LogRequestsMiddleware

# FastAPI application instance
app = FastAPI()

# Add middleware to log incoming requests
app.add_middleware(LogRequestsMiddleware)

# Include router for download operations
# Tags are used for grouping related routes in the API documentation
app.include_router(DownloadRouter, tags=["download"])

# Include router for upload operations
# Tags are used for grouping related routes in the API documentation
app.include_router(UploadRouter, tags=["upload"])

# Include router for delete operations
# Tags are used for grouping related routes in the API documentation
app.include_router(DeleteRouter, tags=["delete"])

# Include router for other operations
# Tags are used for grouping related routes in the API documentation
app.include_router(OthersRouter, tags=["others"])






