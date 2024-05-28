from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
from colorama import Fore, init

from ..models.requests import Requests
from ..libs.database import Session

init(autoreset=True)

class LogRequestsMiddleware(BaseHTTPMiddleware):
    """
    A middleware for logging requests in FastAPI applications.

    This middleware captures and logs details about each HTTP request processed by the FastAPI application.
    It records the request path, method, processing time, client host, and user agent to a database.
    Additionally, it prints a log message to the console indicating the completion time of each request.

    Attributes:
        None

    Methods:
        async dispatch(request: Request, call_next): Processes the incoming request, logs details to the database,
                                                     and prints the processing time to the console.
    """

    async def dispatch(self, request: Request, call_next):
        """
        Process the incoming request, log its details, and calculate its processing time.
        TODO: Add an api to the geolocation of the client.

        Args:
            request (Request): The incoming HTTP request.
            call_next: A function that receives the request and returns the response.

        Returns:
            Response: The HTTP response after processing the request and logging its details.
        """
        # Record the start time of the request
        start_time = time.time()
        # Await the response from the next middleware or endpoint
        response = await call_next(request)
        # Calculate the processing time
        process_time = time.time() - start_time

        # Extract the User-Agent from the request headers
        user_agent = request.headers.get("User-Agent")
        # Log the request details to the database
        with Session() as db:
            data = Requests(path=request.base_url.path, method=request.method, process_time=process_time, host=request.client.host, user_agent=user_agent)
            db.add(data)
            db.commit()
            db.close()
        return response