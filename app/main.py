from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.config import settings


def create_app(api_router: APIRouter) -> FastAPI:
    """Create the application."""
    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app


app = create_app(api_router)
