from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:str| None = None
    price:float
    tax:float| None=None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        final_price = item.tax + item.price
        item_dict.update({'final_price':final_price})
    return item_dict