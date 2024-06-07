from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
from colorama import Fore, init
init(autoreset=True)


class LogRequestsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(Fore.GREEN + "INFO", ":     ", Fore.LIGHTWHITE_EX + f"Completed in {process_time:.4f} secs", sep="")
        return response