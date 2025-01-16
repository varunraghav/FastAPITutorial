from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

#The FilterParams class is a Pydantic model that validates and enforces constraints on query parameters.
#  It defines the structure of the expected query parameters for the /items/ endpoint.

#"extra": "forbid" ensures that no unexpected query parameters can be passed.
    #If a client sends a query parameter not defined in the model, FastAPI will return a validation error.
    #, if the client tries to send a tool query parameter with a value of plumbus, like:
    #https://example.com/items/?limit=10&tool=plumbus
    #They will receive an error response telling them that the query parameter tool is not allowed:

#Model request - http://127.0.0.1:8000/items/?limit=10&offset=2&order_by=updated_at&tags=python,fastapi



class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

"""
order_by:
A literal type that restricts the allowed values to "created_at" or "updated_at".
Default value: "created_at

filter_query: This is an instance of FilterParams, annotated with Query() to indicate it comes from query parameters.

Behavior: FastAPI automatically maps query parameters to the FilterParams model, validates the input, and raises an error 
if the input doesn't meet the constraints defined in FilterParams.

The endpoint returns the validated query parameters as a JSON object.

"""