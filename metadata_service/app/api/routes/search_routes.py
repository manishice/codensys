from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.search_service import search_datasets
from app.api.dependencies import get_db

router = APIRouter()


@router.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    return search_datasets(db, q)