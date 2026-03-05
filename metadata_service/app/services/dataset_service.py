from app.models.dataset import Dataset
from app.models.column import ColumnModel


from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def create_dataset(db, data):

    parts = data.fqn.split(".")

    if len(parts) != 4:
        raise HTTPException(
            status_code=400,
            detail="Invalid FQN format. Expected connection.database.schema.table"
        )

    existing = db.query(Dataset).filter(Dataset.fqn == data.fqn).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Dataset already exists"
        )

    dataset = Dataset(
        fqn=data.fqn,
        connection_name=parts[0],
        database_name=parts[1],
        schema_name=parts[2],
        table_name=parts[3],
        source_type=data.source_type
    )

    try:
        db.add(dataset)
        db.flush()  # get dataset.id before commit

        for col in data.columns:
            column = ColumnModel(
                dataset_id=dataset.id,
                name=col.name,
                type=col.type
            )
            db.add(column)

        db.commit()
        db.refresh(dataset)

        return dataset

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error occurred"
        )