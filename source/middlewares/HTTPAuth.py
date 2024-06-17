from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

import os

KEY = os.getenv("KEY")

class HTTPAuth(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if auth.credentials != KEY:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")