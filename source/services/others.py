from fastapi.responses import RedirectResponse

class Others:
    @staticmethod
    def docs() -> RedirectResponse:
        """
        Redirects the request to the auto-generated documentation page of the FastAPI application.

        This method is useful for providing a convenient shortcut to the FastAPI's Swagger UI documentation,
        which is typically available at the '/docs' endpoint.

        Returns:
        - A RedirectResponse object that redirects the client to the '/docs' URL.
        """
        return RedirectResponse(url="/docs")