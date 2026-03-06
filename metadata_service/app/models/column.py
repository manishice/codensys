from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class ColumnModel(Base):
    __tablename__ = "columns"

    id = Column(Integer, primary_key=True)

    dataset_id = Column(Integer, ForeignKey("datasets.id"))

    name = Column(String(100))
    type = Column(String(50))
