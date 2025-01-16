"""
Path(...): Adds extra validation, constraints, and documentation for the path parameter.
title="The ID of the item to get": Adds a description for item_id in the automatically generated API docs.

alias="item-query": Allows the client to use item-query as the query parameter name in the URL.

#http://127.0.0.1:8000/items/42?item-query=test - {"item_id":42,"q":"test"}

With Query and Path (and others you'll see later) you can declare number constraints.

Here, with ge=1, item_id will need to be an integer number "greater than or equal" to 1.
le: less than or equal

http://127.0.0.1:8000/items/0?item-query=test - {"detail":[{"type":"greater_than_equal","loc":["path","item_id"],"msg":"Input should be greater than or equal to 1","input":"0","ctx":{"ge":1}}]}


"""

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, lt=50)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


