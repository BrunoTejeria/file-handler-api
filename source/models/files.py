from sqlalchemy import create_engine, Column, Integer, String, DateTime
import datetime

from .base import Base

class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    creation_date = Column(DateTime, index=True, default=datetime.datetime.now(), nullable=False)
    created_by = Column(String, default="127.0.0.1")
    