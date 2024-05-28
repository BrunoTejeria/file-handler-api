from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

from ..models.base import Base
from ..models.files import Files
from ..models.requests import Requests
from ..utils.env import __env__

"""
This module sets up the database connection and session management for the application using SQLAlchemy.

It defines the database URL and connection parameters, initializes the SQLAlchemy engine with these parameters, and creates a session factory for interacting with the database. The module also imports the base model and specific models for 'files' and 'requests' to ensure that their tables are created in the database.

Attributes:
    DATABASE_URL (str): A placeholder string for the SQLite database URL. This is not used in the final database connection but serves as an example of how to define a simple SQLite connection.
    DATABASE_CONN (URL): The actual database connection URL, created using SQLAlchemy's URL.create method. It is configured with parameters such as username, password, host, and database name, which are retrieved from the environment variables.
    engine (Engine): The SQLAlchemy engine, created with the DATABASE_CONN parameters. This engine is used to interact with the database.
    Session (sessionmaker): A configured sessionmaker factory, which will produce new Session objects when called. These sessions are bound to the engine and are configured not to autocommit or autoflush, providing more control over transactions.

Usage:
    This setup is used to connect to a PostgreSQL database, but it can be easily adapted to other database systems by changing the DATABASE_CONN parameters. The engine is used to bind the base model's metadata to the database, effectively creating the tables defined in the models if they do not already exist. The Session factory is used throughout the application to create sessions for database transactions, allowing for querying, adding, and modifying records in a controlled manner.
"""

DATABASE_URL = "sqlite:///./db.db"  # NOTE: use this for testing but enable DATABASE_CONN for production.
DATABASE_CONN = URL.create(
    'postgresql',
    username=__env__["database"]["username"],
    password=__env__["database"]["password"],
    host=__env__["database"]["host"],
    database=__env__["database"]["database"]
)

engine = create_engine(DATABASE_CONN)  # Create the SQLAlchemy engine with PostgreSQL connection
Base.metadata.create_all(bind=engine)  # Create all tables in the database based on models
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Create a sessionmaker factory

