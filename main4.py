"""
FastAPI Program: Calculate Final Price for Items

Description:
This program demonstrates how to create an API to handle item creation and calculate a final price 
if a tax is provided. The `Item` model uses Pydantic for data validation.

Endpoints:
1. POST /items/ - Accepts item details (name, description, price, tax) and returns the item data.
   - If `tax` is provided, it calculates the final price (`price + tax`) and includes it in the response.
"""

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