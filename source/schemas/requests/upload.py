from pydantic import BaseModel

class Schemas:
    class Upload(BaseModel):
        name: str
        description: str
        tags: list