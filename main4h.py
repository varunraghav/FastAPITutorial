"""

FastAPI Program: Update Items with Optional Query Parameter

Description:
This program provides an API endpoint to update item details using a combination of:
1. Path parameters (`item_id`) to specify the item being updated.
2. Request body (`item`) to provide the updated item details.
3. Optional query parameters (`q`) to include additional metadata.

Endpoints:
1. PUT /items/{item_id} - Updates item details and optionally includes the query parameter `q` in the response.

"""

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result