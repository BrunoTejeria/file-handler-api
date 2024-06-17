from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from ..utils.env import __env__

class HTTPAuth(HTTPBearer):
    """
    Implements API key-based authentication for FastAPI endpoints.

    This class overrides the default behavior of HTTPBearer to include a check
    against a predefined API key. It ensures that only requests with valid
    credentials can access certain endpoints.

    The API key is expected to be provided in the Authorization header of the request.
    If the provided API key does not match the expected value, the request is rejected
    with a 403 Forbidden status.
    """
    async def __call__(self, request: Request):
        """
        Asynchronously validates the API key provided in the request's Authorization header.

        Args:
            request (Request): The incoming request object.

        Raises:
            HTTPException: 403 error if the provided API key does not match the expected value.
        """
        auth = await super().__call__(request)
        if auth.credentials != __env__['auth']['api_key']:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")