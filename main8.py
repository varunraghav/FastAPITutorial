"""
FastAPI Program: Path and Body Parameters

This program demonstrates:
1. Path parameters with metadata and validation.
2. Body parameters with single and multiple Pydantic models.
3. Use of `Body()` for additional metadata and embedded JSON structures.

Endpoints:
1. PUT /items/{item_id} - Update an item with optional query and body parameters.
2. PUT /items2/{item_id} - Update item and user details using Pydantic models.
3. PUT /items3/{item_id} - Update item, user, and additional importance parameter.
4. PUT /items4/{item_id} - Use `Body(embed=True)` to modify request structure.
"""


from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

#In the belows example, the path operations would expect a JSON body with the attributes of an Item,
#  like:
#{
#    "name": "Foo",
#    "description": "The pretender",
#    "price": 42.0,
#    "tax": 3.2
#}


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


#In this case, FastAPI will notice that there is more than one body parameter in the function 
# (there are two parameters that are Pydantic models).
#So, it will then use the parameter names as keys (field names) in the body, and expect a body like:
"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
"""

# it will then use the parameter names as keys (field names) in the body, and expect a body like:

"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
"""
@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results



@app.put("/items3/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

#The same way there is a Query and Path to define extra data for query and path parameters,
#  FastAPI provides an equivalent Body.
# Expected output is
"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
"""

@app.put("/items4/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

#But if you want it to expect a JSON with a key item and inside of it the model contents, 
# as it does when you declare extra body parameters, you can use the special Body parameter embed:


"""
In this case FastAPI will expect a body like:


{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
"""