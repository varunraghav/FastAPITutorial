#Program to get started. Run uvicorn main:app --reload to get started. Go to the link on
# Uvicorn running on http://127.0.0.1:8000 to view "Hello World"

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello world"