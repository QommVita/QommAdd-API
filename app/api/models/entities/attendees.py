"""Attendee entity model"""
from pydantic import BaseModel

class AttendeeBase(BaseModel):
    """Base model for Attendee entity."""
    id: int
    name: str
    email: str
    
class AttendeeCreate(AttendeeBase):
    """Model for creating a new Attendee."""

class AttendeeUpdate(AttendeeBase):
    """Model for updating an existing Attendee."""


class AttendeeOut(AttendeeBase):
    """Model for outputting Attendee data."""
    id: int
    class Config:
        """Configuration for Pydantic model."""
        orm_mode = True