from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.lineage_schema import LineageCreate
from app.services.lineage_service import create_lineage
from app.api.dependencies import get_db

router = APIRouter()


@router.post("/lineage")
def add_lineage(data: LineageCreate, db: Session = Depends(get_db)):
    return create_lineage(db, data)
