from sqlalchemy import Column, Integer, Float, String, DateTime
import datetime

from .base import Base

class Requests(Base):
    """
    Represents a 'requests' table in a database using SQLAlchemy.

    Attributes:
        __tablename__ (str): The name of the table in the database, set to 'requests'.
        id (Column): The primary key column, uniquely identifying each request log entry.
        path (Column): The path of the HTTP request.
        method (Column): The HTTP method used for the request (e.g., GET, POST).
        time (Column): The date and time when the request was made, defaulting to the current time.
        process_time (Column): The time taken to process the request, in seconds.
        host (Column): The host IP address from which the request originated.
        city (Column): The city from which the request was made. This is currently optional but intended to be made non-nullable in future updates.
        country (Column): The country from which the request was made. This is also optional for now.
        ISP (Column): The Internet Service Provider of the client making the request. Optional for now.
        latitude (Column): The latitude part of the location from which the request was made. Optional for now.
        longitude (Column): The longitude part of the location from which the request was made. Optional for now.
        timezone (Column): The timezone of the client making the request. Optional for now.
        user_agent (Column): The user agent string of the client, providing details about the client's device, browser, and operating system. Optional for now.

    Usage:
        This class is used to interact with the 'files' table in the database.
    """
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, index=True, nullable=False)
    method = Column(String, index=True, nullable=False)
    time = Column(DateTime, index=True, default=datetime.datetime.now(), nullable=False)
    process_time = Column(Float, index=True, nullable=False)
    host = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    country = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    ISP = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    latitude = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    longitude = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    timezone = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    user_agent = Column(String, index=True, nullable=True) # TODO: no nullable add an api for this
    