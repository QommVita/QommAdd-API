"""API to handle events from a CSV file"""
from typing import List, Dict
import csv
from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse


CSV_PATH = Path("app/api/data/events.csv")
router = APIRouter(prefix="/events", tags=["events"])

def read_csv() -> List[Dict[str, str]]:
    """Reads the CSV file and returns a list of dictionaries"""
    if not CSV_PATH.exists():
        raise HTTPException(status_code=404, detail="CSV file not found")
    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        data = list(csv.DictReader(file))
        if not data:
            raise HTTPException(
                status_code=422, detail="No events found in the CSV file")
        return data

@router.get("/", response_model=List[Dict[str, str]])
async def get_events():
    """ 
    Endpoint to retrieve all events.
    Returns:
        List of all events in the CSV file
    Raises:
        HTTPException: If there's an error reading the file
    """
    try:
        return JSONResponse(read_csv())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{event_id}", response_model=Dict[str, str])
async def get_event(event_id: str):
    """
    Endpoint to retrieve a specific event by ID.
    
    Args:
        event_id: The ID of the event to retrieve
        
    Returns:
        dict: Found event with structure:
            {"id": "1", "name": "Event 1", ...}
            
    Raises:
        HTTPException: 404 if event is not found
    """
    events = read_csv()
    for event in events:
        if event.get("Id") == event_id:
            return JSONResponse(event)
    raise HTTPException(status_code=404, detail="Event not found")