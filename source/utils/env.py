import dotenv
import os

dotenv.load_dotenv()

# env file:
"""
# Files
MAX_FILE_SIZE = 1000000 # 64 MB in Bytes

# Database
POSTGRES_USER=<PSQL.USER>
POSTGRES_PASSWORD=<PSQL.PASSWORD>
POSTGRES_HOST=<PSQL.HOST>
POSTGRES_DB=<PSQL.DB>

# Auth
KEY = <AUTH.KEY>
"""

# env vars in dictionary format
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

