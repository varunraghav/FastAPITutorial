"""
This program demonstrates file upload concept in 2 ways
File():
Reads the entire file content as bytes.
Suitable for small files that can be directly loaded into memory.

UploadFile:
Provides a lightweight object with methods to access the file contents without loading the entire file into memory.
Better for handling larger files.

Go to http://127.0.0.1:8000/docs to try uploading file
"""

from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}