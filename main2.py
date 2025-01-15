from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    if model_name.value == "resnet":
        return {"model_name": model_name, "message": "eniki onnum manasilaayilla"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id+1}

#Let's create a same path operation. This won't be called as the first one would be called
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id+5}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

"""
Because path operations are evaluated in order, 
you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:

Otherwise, the path for /users/{user_id} would match also for /users/me,
 "thinking" that it's receiving a parameter user_id with a value of "me".
"""