from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Activity(Base):
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    event_type = Column(String)
    timestamp = Column(String)
    page = Column(String)
    browser = Column(String)
    
     