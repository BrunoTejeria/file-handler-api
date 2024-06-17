from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from ..utils.env import __env__

class HTTPAuth(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if auth.credentials != __env__['auth']['api_key']:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")