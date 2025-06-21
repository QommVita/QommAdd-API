""""Ticket Type Model"""
from datetime import datetime
from pydantic import BaseModel

class TicketTypeBase(BaseModel):
    """Base model for Ticket Type entity."""
    name: str
    price: float
    available_from: datetime
    available_until: datetime

class TicketTypeCreate(TicketTypeBase):
    """Model for creating a new Ticket Type."""

class TicketTypeOut(TicketTypeBase):
    """Model for outputting Ticket Type data."""
    id: int

    class Config:
        """Configuration for Pydantic model."""
        orm_mode = True