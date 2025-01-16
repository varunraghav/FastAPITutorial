"""
FastAPI Program: Using Pydantic's Field for Validation and Metadata

Demonstrates:
1. Validation and metadata for model fields using `Field`.
2. Embedding request bodies with `Body(embed=True)`.

Endpoint:
- **PUT /items/{item_id}**: Updates an item with validation on:
  - `description` (max length: 300).
  - `price` (must be > 0).

Request Example:
```json
{
    "item": {
        "name": "Laptop",
        "description": "A high-end gaming laptop",
        "price": 1500.0,
        "tax": 225.0
    }
}
"""


from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

#The same way you can declare additional validation and metadata in path operation function parameters with 
    #   Query, Path and Body, 
# you can declare validation and metadata inside of Pydantic models using Pydantic's Field.


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results