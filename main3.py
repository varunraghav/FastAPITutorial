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