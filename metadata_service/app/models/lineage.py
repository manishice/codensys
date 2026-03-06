from sqlalchemy import Column, Integer, ForeignKey
from app.database.base import Base


class Lineage(Base):
    __tablename__ = "lineage"

    id = Column(Integer, primary_key=True)

    upstream_dataset_id = Column(Integer, ForeignKey("datasets.id"))

    downstream_dataset_id = Column(Integer, ForeignKey("datasets.id"))
