from sqlalchemy import create_engine, Column, Integer, String, DateTime
import datetime

from .base import Base

class Files(Base):
    """
    Represents a 'files' table in a database using SQLAlchemy.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (Column): The primary key column of the table, which uniquely identifies each record.
        name (Column): A column storing the name of the file. It is indexed to improve query performance.
        creation_date (Column): A column storing the date and time when the file was created. It defaults to the current date and time when the record is inserted.
        created_by (Column): A column storing the IP address of the user who created the file. It defaults to '127.0.0.1'.

    Usage:
        This class is used to interact with the 'files' table in the database.
    """
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    creation_date = Column(DateTime, index=True, default=datetime.datetime.now(), nullable=False)
    created_by = Column(String, default="127.0.0.1")