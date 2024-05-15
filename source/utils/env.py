import dotenv
import os

dotenv.load_dotenv()

__env__ = {
    "FILES_FOLDER": os.getenv("FILES_FOLDER"),
    "database": {
        "username":os.getenv('POSTGRES_USER'),
        "password":os.getenv('POSTGRES_PASSWORD'),
        "host":os.getenv('POSTGRES_HOST'),
        "database":os.getenv('POSTGRES_DB')
    }
}

