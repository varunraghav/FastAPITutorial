"""
FastAPI Program: Query and Path Parameters Demonstration

This program demonstrates the use of:
1. Query parameters for filtering and optional inputs.
2. Path parameters for identifying specific resources.
3. Automatic validation of parameters by FastAPI.

Endpoints:
1. **GET /items/**: Retrieve items from a database with pagination (`skip`, `limit`).
2. **GET /itemsnn/{item_id}**: Fetch item details using `item_id` and optional `q` and `short` query parameters.
3. **GET /itemsrq/{item_id}**: Retrieve an item with a required query parameter `needy`.

"""

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#http://127.0.0.1:8000/items/book - 
# {"detail":[{"type":"int_parsing","loc":["path","item_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"book"}]}

@app.get("/itemsnn/{item_id}")
async def read_item_nn(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#http://127.0.0.1:8000/itemsnn/123?q=test_query - #{"item_id":"123","q":"test_query"}
#http://127.0.0.1:8000/itemsnn/roti?q=chappati&short=False - {"item_id":"roti","q":"chappati","description":"This is an amazing item that has a long description"}
#http://127.0.0.1:8000/itemsnn/rotii&short=True - {"item_id":"rotii&short=True","description":"This is an amazing item that has a long description"}

@app.get("/itemsrq/{item_id}")
async def read_user_itemrq(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

#http://127.0.0.1:8000/itemsrq/foo-item?needy=yes - {"item_id":"foo-item","needy":"yes"}