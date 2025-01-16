"""
This program defines an API endpoint /login/ that expects a POST request with form data.
 The FormData Pydantic model is used to structure and validate the incoming data. 
"""

from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# Define the FormData model for validation
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


@app.post("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    # Validate using the FormData Pydantic model
    data = FormData(username=username, password=password)
    return data.dict()
