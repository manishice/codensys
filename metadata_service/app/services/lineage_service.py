from fastapi import HTTPException
from app.models.dataset import Dataset
from app.models.lineage import Lineage

from sqlalchemy.exc import SQLAlchemyError


def detect_cycle(db, upstream_id, downstream_id):

    stack = [downstream_id]
    visited = set()

    while stack:
        node = stack.pop()

        if node == upstream_id:
            return True

        if node in visited:
            continue

        visited.add(node)

        children = db.query(Lineage).filter(Lineage.upstream_dataset_id == node).all()

        for child in children:
            stack.append(child.downstream_dataset_id)

    return False


def create_lineage(db, data):

    upstream = db.query(Dataset).filter(Dataset.fqn == data.upstream_dataset).first()

    downstream = (
        db.query(Dataset).filter(Dataset.fqn == data.downstream_dataset).first()
    )

    if not upstream or not downstream:
        raise HTTPException(status_code=404, detail="Dataset not found")

    if upstream.id == downstream.id:
        raise HTTPException(
            status_code=400, detail="Upstream and downstream dataset cannot be the same"
        )

    existing = (
        db.query(Lineage)
        .filter(
            Lineage.upstream_dataset_id == upstream.id,
            Lineage.downstream_dataset_id == downstream.id,
        )
        .first()
    )

    if existing:
        raise HTTPException(status_code=400, detail="Lineage already exists")

    if detect_cycle(db, upstream.id, downstream.id):
        raise HTTPException(status_code=400, detail="Invalid lineage: cycle detected")

    lineage = Lineage(
        upstream_dataset_id=upstream.id, downstream_dataset_id=downstream.id
    )

    try:
        db.add(lineage)
        db.commit()
        return {"message": "Lineage created successfully"}

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
