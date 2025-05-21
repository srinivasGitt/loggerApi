from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .schemas import EventCreate
from .models import Activity
from .database import SessionLocal
import re

router = APIRouter()

#Simulated user DB

USER_DATABASE = {'alice', 'ravi', 'john'}
ALLOWED_EVENT_TYPES = {'page_view', "click", 'form_submit'}


def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/user/{username}/activity")
def record_activity(username: str, event: EventCreate, db:Session = Depends(get_db)):
    if username not in USER_DATABASE:
        raise
    HTTPException(status_code=404, detail="user not found")
    
    if event.event_type not in ALLOWED_EVENT_TYPES:
        raise
    HTTPException(status_code=404, detail="invalid event type")
    
    try:
        datetime.fromisoformat(event.timestamp.replace("z", "+00.00"))
    except ValueError:
        raise
    HTTPException(status_code=400, detail="invalid time stamp")
    
    activity = Activity(
        username=username,
        event_type= event.event_type,
        timestamp = event.timestamp,
        page= event.metadata.page,
        browser = event.metadata.browser
    )
    db.add(activity)
    db.commit()
    
    return {"message": "activity recorded"}


    
    