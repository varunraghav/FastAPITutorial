"""
FastAPI Comprehensive Metadata Example:
This program demonstrates how to add metadata to path operations in FastAPI,
including:
1. Tags: Grouping operations for better documentation.
2. Response Status Code: Specifying HTTP status codes for responses.
3. Summary: A brief summary of what the endpoint does.
4. Description: Detailed information about the endpoint's purpose.
5. Response Description: Describing the format and content of responses.

This isn't much significant in the longer run, it's just another way of decorating your docs

Endpoints:
1. Create an item.
2. Get an item by ID.
3. List all items.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ----------------------
# Pydantic Models
# ----------------------

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# In-memory database for demonstration purposes
items_db: List[Item] = []

# ----------------------
# Path Operations
# ----------------------

@app.post(
    "/items/",
    response_model=Item,
    status_code=201,
    tags=["Items"],
    summary="Create a new item",
    description="This endpoint allows you to create a new item by providing the item's details. "
                "The created item will be returned in the response.",
    response_description="The created item, including its ID, name, description, price, and tax.",
)
async def create_item(item: Item) -> Item:
    """
    Creates a new item and stores it in the database.

    Request Body:
    {
        "id": 1,
        "name": "Laptop",
        "description": "A high-end gaming laptop",
        "price": 1500.00,
        "tax": 225.00
    }

    Response:
    {
        "id": 1,
        "name": "Laptop",
        "description": "A high-end gaming laptop",
        "price": 1500.00,
        "tax": 225.00
    }
    """
    items_db.append(item)
    return item


@app.get(
    "/items/{item_id}",
    response_model=Item,
    status_code=200,
    tags=["Items"],
    summary="Retrieve an item by ID",
    description="Fetch the details of a specific item by providing its unique ID.",
    response_description="The item details, including its ID, name, description, price, and tax.",
)
async def get_item(item_id: int) -> Item:
    """
    Retrieves an item by its ID.

    Path Parameter:
    - item_id (int): The unique ID of the item to retrieve.

    Response:
    - 200: The details of the requested item.
    - 404: If the item is not found.
    """
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")


@app.get(
    "/items/",
    response_model=List[Item],
    status_code=200,
    tags=["Items"],
    summary="List all items",
    description="Retrieve a list of all items currently stored in the database.",
    response_description="A list of all items, with their IDs, names, descriptions, prices, and taxes.",
)
async def list_items() -> List[Item]:
    """
    Lists all items in the database.

    Response:
    - 200: A list of all items.
    """
    return items_db

# ----------------------
# Example Data for Testing
# ----------------------

@app.on_event("startup")
async def populate_example_data():
    """Pre-populates the in-memory database with example items for testing."""
    items_db.extend([
        Item(id=1, name="Phone", description="A smartphone with a great camera", price=700.00, tax=105.00),
        Item(id=2, name="Tablet", description="A tablet for media consumption", price=300.00, tax=45.00),
    ])
