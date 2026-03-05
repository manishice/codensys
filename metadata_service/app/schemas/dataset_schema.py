from pydantic import BaseModel
from typing import List


class ColumnCreate(BaseModel):
    name: str
    type: str


class DatasetCreate(BaseModel):
    fqn: str
    source_type: str
    columns: List[ColumnCreate]