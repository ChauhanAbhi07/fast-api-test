# app/main.py

from fastapi import FastAPI
import handlers

app = FastAPI(
    title="Testing",
    description="API for E-Way Bill generation and operations.",
    version="1.0.0",
    docs_url="/docs",              # Swagger UI
    redoc_url="/redoc",            # Optional: ReDoc UI
    openapi_url="/openapi.json"    # OpenAPI spec
)

# app = FastAPI(
#     title="CRUD Names API",
#     description="A simple FastAPI app with layered architecture",
#     version="1.0.0",
# )

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001"],  # or ["*"] for development only
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(handlers.router)
