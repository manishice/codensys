from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.dataset_schema import DatasetCreate
from app.services.dataset_service import create_dataset
from app.database.session import SessionLocal
from app.api.dependencies import get_db


router = APIRouter()


@router.post("/datasets")
def add_dataset(data: DatasetCreate, db: Session = Depends(get_db)):
    return create_dataset(db, data)