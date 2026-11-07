from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import init_db
from routers import categories, recipes


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Online Recipe Book API",
    description="""
    An advanced recipe management system
    built using FastAPI, Pydantic and SQLite.

    Features:
    - Recipe management
    - Category management
    - Search and filtering
    - Data validation
    """,
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Online Recipe Book API!",
        "documentation": "/docs"
    }


app.include_router(categories.router)
app.include_router(recipes.router)