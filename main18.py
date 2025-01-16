"""
Unified Program Demonstrating `jsonable_encoder`:
1. Example 1: Stores events using `jsonable_encoder` to ensure JSON compatibility.
2. Example 2: Updates and retrieves items using `jsonable_encoder`.

Key Feature:
`jsonable_encoder` ensures that complex types (e.g., `datetime`, `None`) are converted into JSON-compatible formats.
"""

from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ----------------------
# Example 1: Event Management
# ----------------------

class Event(BaseModel):
    name: str
    date: datetime

events = {}

@app.post("/events/{id}")
def create_event(id: str, event: Event):
    # Convert to JSON-compatible format
    json_event = jsonable_encoder(event)
    events[id] = json_event
    return {"status": "Event stored", "event": json_event}

# ----------------------
# Example 2: Item Management
# ----------------------

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

# ----------------------
# Testing Data
# ----------------------

@app.on_event("startup")
async def populate_example_data():
    # Populate events
    events["1"] = jsonable_encoder(
        Event(name="FastAPI Meetup", date=datetime(2025, 1, 12, 14, 30))
    )
