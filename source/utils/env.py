import dotenv
import os

dotenv.load_dotenv()

__env__ = {
    "files": {
        "max_size": int(eval(os.getenv('MAX_FILE_SIZE'))),
    },
    "database": {
        "username":os.getenv('POSTGRES_USER'),
        "password":os.getenv('POSTGRES_PASSWORD'),
        "host":os.getenv('POSTGRES_HOST'),
        "database":os.getenv('POSTGRES_DB')
    },
    "auth": {
        "api_key": os.getenv("KEY")
    }
}

