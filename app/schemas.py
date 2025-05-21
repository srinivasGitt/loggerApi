from pydantic import BaseModel, Field


class Metadata(BaseModel):
    page:str
    browser: str

class EventCreate(BaseModel):
    event_type: str = Field(...,example='page_view')
    timestamp: str = Field(..., example='2025-05-15T10:12:00Z')
    metadata: Metadata
    