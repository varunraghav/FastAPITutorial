"""
This FastAPI application demonstrates the use of Cookie parameters for extracting
and validating data from HTTP cookies. It includes three endpoints:

1. /extract-with-cookie/:
   Extracts cookies using the FastAPI `Cookie` parameter utility.
   Automatically validates cookies using a Pydantic model.

2. /extract-without-cookie/:
   Extracts cookies manually from the request headers and validates them using a Pydantic model.
   This method doesn't generate Swagger documentation for cookie parameters.

3. /mymethod/:
   Illustrates an incorrect approach to extract cookies directly using a Pydantic model.
   This endpoint demonstrates why explicit use of `Cookie` parameters is necessary.

The code highlights the benefits of using `Cookie` parameters for automatic extraction, 
validation, and inclusion in Swagger documentation.

To implement this, go to a new Terminal, type
curl -X GET "http://127.0.0.1:8000/extract-with-cookie/" \
-H "Cookie: session_id=abc123; fatebook_tracker=tracker123; googall_tracker=tracker456"

"""
from fastapi import FastAPI, Cookie, Request
from pydantic import BaseModel, ValidationError

app = FastAPI()

# Define the Pydantic model for cookies
class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

@app.get("/extract-with-cookie/")
async def extract_with_cookie(
    session_id: str = Cookie(...),
    fatebook_tracker: str | None = Cookie(default=None),
    googall_tracker: str | None = Cookie(default=None),
):
    # Use the Pydantic model for structured validation
    cookies = Cookies(
        session_id=session_id,
        fatebook_tracker=fatebook_tracker,
        googall_tracker=googall_tracker,
    )
    return {"cookies": cookies.dict()}



@app.get("/extract-without-cookie/")
async def extract_without_cookie(request: Request):
    cookie_header = request.headers.get("cookie")
    if not cookie_header:
        return {"error": "No cookies provided"}

    # Parse cookies manually
    cookies_dict = {}
    for cookie in cookie_header.split("; "):
        key, value = cookie.split("=")
        cookies_dict[key] = value

    # Validate cookies using Pydantic
    try:
        cookies = Cookies(**cookies_dict)
    except ValidationError as e:
        return {"error": "Invalid cookies", "details": e.errors()}

    return {"cookies": cookies.dict()}

@app.get("/mymethod/")
async def extract_my_method(cook: Cookies):
    request_dict = cook.dict()
    return request_dict

