# FastAPI Project Skeleton

Industry-grade FastAPI project skeleton with versioned API, centralized config, logging, and exception handling.

## Features

- **FastAPI** with Python 3.9+
- **API Versioning** (`/api/v1`)
- **Pydantic Settings** for configuration
- **Structlog** for structured logging (JSON in production)
- **Global Exception Handling**
- **CORS** enabled
- **Health Check** endpoint

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd Backend-Lucid
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

## API Documentation

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure

```
app/
├── api/            # API handlers
│   └── v1/
│       ├── endpoints/
│       └── router.py
├── core/           # Core functionality (config, logging, etc.)
└── main.py         # Application entry point
```
# backend-lucid
