from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from ..utils.responses import Responses
from ..schemas.data_validators import Validators


router = APIRouter()
