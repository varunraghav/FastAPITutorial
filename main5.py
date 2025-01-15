#We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=10, pattern="^varun")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#http://127.0.0.1:8000/items/?q=varunraghav - {"detail":[{"type":"string_too_long","loc":["query","q"],"msg":"String should have at most 10 characters","input":"varunraghav","ctx":{"max_length":10}}]}
#http://127.0.0.1:8000/items/?q=varun - {"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"varun"}
#http://127.0.0.1:8000/items/?q=va - {"detail":[{"type":"string_too_short","loc":["query","q"],"msg":"String should have at least 3 characters","input":"va","ctx":{"min_length":3}}]}
#http://127.0.0.1:8000/items/?q=varuba - {"detail":[{"type":"string_pattern_mismatch","loc":["query","q"],"msg":"String should match pattern '^varun'","input":"varuba","ctx":{"pattern":"^varun"}}]}

@app.get("/items2/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


#http://localhost:8000/items2/?q=foo&q=bar - {"q":["foo","bar"]}

@app.get("/items3/")
async def read_items(
    q: Annotated[
        str | None, 
        Query(
            title="Query String", 
            description="Query string for the items to search in the database that have a good match",
            min_length=3
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#You can add more information about the parameter.
#That information will be included in the generated OpenAPI and used by the documentation user interfaces and external tools.

@app.get("/items4/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
