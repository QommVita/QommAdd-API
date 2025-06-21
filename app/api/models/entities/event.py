"""Model for Event entity."""
from datetime import datetime
from typing import List
from pydantic import BaseModel
from app.api.models.entities.ticket import TicketTypeOut
from app.api.models.entities.attendees import AttendeeOut

class EventBase(BaseModel):
    """Base model for Event entity."""
    title: str
    description: str | None = None
    location: str | None = None
    start_time: datetime
    end_time: datetime
    host: str | None = None

class EventCreate(EventBase):
    """Base model for Event entity."""
    
class EventUpdate(EventBase):
    """Base model for Event entity."""

class EventOut(EventBase):
    """Base model for Event entity."""
    id: int
    ticket_types: List[TicketTypeOut] =[]
    attendees: List[AttendeeOut] = []

    class Config:
        """Configuration for Pydantic model."""
        orm_mode = True
