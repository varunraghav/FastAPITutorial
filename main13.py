"""
Headers are used for metadata about the request (e.g., authentication, content type, caching policies). They are not part of the request data itself.
Example: Headers are like instructions about how the client is sending the request.
Query Parameters are part of the URL and are used to specify data related to the resource being fetched or acted upon.
Example: Query parameters describe what data you want to retrieve.

1. Use headers to pass sensitive data like tokens.
2. Headers can include information about the request context, like:
    User-Agent (browser or client details).
    Content-Type (data format being sent).

"""

from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers