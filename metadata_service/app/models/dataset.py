from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    fqn = Column(String(255), unique=True, nullable=False)

    connection_name = Column(String(100))
    database_name = Column(String(100))
    schema_name = Column(String(100))
    table_name = Column(String(100))

    source_type = Column(String(50))
