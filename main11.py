"""
This program demonstrates how you can use examples of the input you would like user to pass.
This is useful as it gets automatically populated in API docs.

It can be used anywhere
1. First example shows it's used in Field
2. Second example shows how it can be used inside Body - that too multiple examples
3. 3rd example uses a different approach of defining examples using Openapi example, which is more comprehensive
"""
from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item_first(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results



class ItemSecond(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items2/{item_id}")
async def update_item_second(
    *,
    item_id: int,
    item: Annotated[
        ItemSecond,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ],
        ),
    ],
):
    results2 = {"item_id": item_id, "item": item}
    return results2

class ItemThird(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None



@app.put("/items3/{item_id}")
async def update_item_third(
    *,
    item_id: int,
    item: Annotated[
        ItemThird,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results3 = {"item_id": item_id, "item": item}
    return results3