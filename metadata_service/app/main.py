from fastapi import FastAPI

from app.api.routes.dataset_routes import router as database_router
from app.api.routes.lineage_routes import router as lineage_router
from app.api.routes.search_routes import router as search_router

app = FastAPI(title="Metadata Service")

app.include_router(database_router, prefix="/api/v1")
app.include_router(lineage_router, prefix="/api/v1")
app.include_router(search_router, prefix="/api/v1")