from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
from colorama import Fore, init

from ..models.requests import Requests
from ..libs.database import Session

init(autoreset=True)


class LogRequestsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        user_agent = request.headers.get("User-Agent")
        with Session() as db:
            data = Requests(path=request.base_url.path, method=request.method, process_time=process_time, host=request.client.host, user_agent=user_agent)
            db.add(data)
            db.commit()
            db.close()
        print(Fore.GREEN + "INFO", ":     ", Fore.LIGHTWHITE_EX + f"Completed in {process_time:.4f} secs", sep="")
        return response
