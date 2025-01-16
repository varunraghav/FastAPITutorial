# FastAPI Tutorial

This repository contains a comprehensive tutorial on FastAPI, demonstrating various features and concepts through practical examples.

## Getting Started

To run any of the programs:

```bash
uvicorn main:app --reload
```

Access the API documentation at: http://127.0.0.1:8000/docs

## Program Contents

### Basic Concepts
- `main.py`: Basic "Hello World" application to get started with FastAPI
- `main2.py`: Introduction to path operations and path parameters
- `main3.py`: Fundamentals of query parameters

### Request Handling
- `main4.py`: Item creation API with price calculation using Pydantic models
- `main4h.py`: Updating items using path parameters, request body, and optional query parameters
- `main5.py`: Advanced query parameter features including validation rules, optional parameters, and metadata
- `main6.py`: Path parameter validation and constraints using Path()
- `main7.py`: Query parameter validation using Pydantic models with FilterParams

### Data Models and Validation
- `main8.py`: Path and body parameters with Pydantic models and Body() usage
- `main9.py`: Field validation and metadata using Pydantic's Field
- `main10.py`: Nested models and type hints for complex data structures
- `main11.py`: Request body examples and documentation using Field, Body, and OpenAPI

### Request Components
- `main12.py`: Working with cookies and cookie parameter validation
- `main13.py`: Understanding headers and their usage for metadata
- `main14.py`: Response models for filtering and validating API responses
- `main15.py`: Form data handling and validation

### Advanced Features
- `main16.py`: File upload handling using File() and UploadFile
- `main17.py`: API metadata including tags, status codes, and documentation
- `main18.py`: JSON encoding with jsonable_encoder for complex data types

## Key Features Covered

- Path Operations and Parameters
- Query Parameters
- Request Bodies
- Data Validation
- Response Models
- Form Data
- File Uploads
- Headers and Cookies
- API Documentation
- JSON Handling
- Type Hints and Pydantic Models

## Prerequisites

- Python 3.9+
- FastAPI
- Uvicorn

## Additional Notes

Each program file contains detailed documentation and examples. The API documentation (Swagger UI) is automatically generated and can be accessed at the /docs endpoint when running any of the programs.
