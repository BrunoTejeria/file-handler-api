from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse

from ..utils.responses import Responses
from ..schemas.data_validators import Validators


router = APIRouter()


@router.get("/", tags=["others"])
def docs(request: Request, response: Response):
    return RedirectResponse(url="/docs")