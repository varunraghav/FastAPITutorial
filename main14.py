"""
FastAPI Demonstration of response_model:
This application demonstrates the use of `response_model` for filtering and validating responses,
as well as examples of not using `response_model`. It includes:

1. POST /items/ - Create an item (with and without `response_model`).
2. GET /items/ - Retrieve a list of items (with and without `response_model`).
3. POST /user/ - Create a user with secure response filtering.

Each section contains sample requests and responses for clarity.
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

# ------------------------------------------------------------
# Item Models and Endpoints
# ------------------------------------------------------------

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

# --- Without response_model ---
@app.post("/items/no-response-model/")
async def create_item_no_response_model(item: Item) -> Item:
    """
    Create an item (without `response_model`).

    Request:
    {
        "name": "Portal Gun",
        "description": "A device for interdimensional travel",
        "price": 42.0,
        "tax": 4.2,
        "tags": ["sci-fi", "gadget"]
    }

    Response (includes all fields, even extra ones if provided):
    {
        "name": "Portal Gun",
        "description": "A device for interdimensional travel",
        "price": 42.0,
        "tax": 4.2,
        "tags": ["sci-fi", "gadget"]
    }
    """
    return item

@app.get("/items/no-response-model/")
async def read_items_no_response_model() -> list[Item]:
    """
    Retrieve items (without `response_model`).

    Response:
    [
        {
            "name": "Portal Gun",
            "description": null,
            "price": 42.0,
            "tax": null,
            "tags": []
        },
        {
            "name": "Plumbus",
            "description": null,
            "price": 32.0,
            "tax": null,
            "tags": []
        }
    ]
    """
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# --- With response_model ---
@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    """
    Create an item (with `response_model`).

    Request:
    {
        "name": "Portal Gun",
        "description": "A device for interdimensional travel",
        "price": 42.0,
        "tax": 4.2,
        "tags": ["sci-fi", "gadget"]
    }

    Response:
    {
        "name": "Portal Gun",
        "description": "A device for interdimensional travel",
        "price": 42.0,
        "tax": 4.2,
        "tags": ["sci-fi", "gadget"]
    }
    """
    return item

@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    """
    Retrieve a list of items (with `response_model`).

    Response:
    [
        {
            "name": "Portal Gun",
            "description": null,
            "price": 42.0,
            "tax": null,
            "tags": []
        },
        {
            "name": "Plumbus",
            "description": null,
            "price": 32.0,
            "tax": null,
            "tags": []
        }
    ]
    """
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# ------------------------------------------------------------
# User Models and Endpoints
# ------------------------------------------------------------

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# --- Without response_model ---
@app.post("/user/no-response-model/")
async def create_user_no_response_model(user: UserIn) -> UserIn:
    """
    Create a user (without `response_model`).

    Request:
    {
        "username": "johndoe",
        "password": "supersecret",
        "email": "john.doe@example.com",
        "full_name": "John Doe"
    }

    Response (includes sensitive fields like `password`):
    {
        "username": "johndoe",
        "password": "supersecret",
        "email": "john.doe@example.com",
        "full_name": "John Doe"
    }
    """
    return user

# --- With response_model ---
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    """
    Create a user (with `response_model` to filter sensitive fields).

    Request:
    {
        "username": "johndoe",
        "password": "supersecret",
        "email": "john.doe@example.com",
        "full_name": "John Doe"
    }

    Response (hides sensitive fields like `password`):
    {
        "username": "johndoe",
        "email": "john.doe@example.com",
        "full_name": "John Doe"
    }
    """
    return user
