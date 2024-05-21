from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

from .models.base import Base
from .models.files import Files
from .models.requests import Requests
from .utils.env import __env__




DATABASE_URL = "sqlite:///./db.db"
DATABASE_CONN = URL.create(
    'postgresql',
    username=__env__["database"]["username"],
    password=__env__["database"]["password"],
    host=__env__["database"]["host"],
    database=__env__["database"]["database"]
)

engine = create_engine(DATABASE_CONN)
Base().metadata.create_all(bind=engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


