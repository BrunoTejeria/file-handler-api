from sqlalchemy import Column, Integer, Float, String, DateTime
import datetime

from .base import Base

class Requests(Base):
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
    