from app.models.dataset import Dataset
from app.models.column import ColumnModel
from app.models.lineage import Lineage


def search_datasets(db, query):

    results = []
    seen = set()

    def add_results(datasets):
        for ds in datasets:
            if ds.id not in seen:
                results.append(ds)
                seen.add(ds.id)

    # Priority 1: Table name
    table_matches = db.query(Dataset).filter(
        Dataset.table_name.ilike(f"%{query}%")
    ).all()
    add_results(table_matches)

    # Priority 2: Column name
    column_matches = (
        db.query(Dataset)
        .join(ColumnModel)
        .filter(ColumnModel.name.ilike(f"%{query}%"))
        .all()
    )
    add_results(column_matches)

    # Priority 3: Schema name
    schema_matches = db.query(Dataset).filter(
        Dataset.schema_name.ilike(f"%{query}%")
    ).all()
    add_results(schema_matches)

    # Priority 4: Database name
    database_matches = db.query(Dataset).filter(
        Dataset.database_name.ilike(f"%{query}%")
    ).all()
    add_results(database_matches)

    response = []

    for ds in results:

        columns = db.query(ColumnModel).filter(
            ColumnModel.dataset_id == ds.id
        ).all()

        upstream = (
            db.query(Dataset)
            .join(Lineage, Lineage.upstream_dataset_id == Dataset.id)
            .filter(Lineage.downstream_dataset_id == ds.id)
            .all()
        )

        downstream = (
            db.query(Dataset)
            .join(Lineage, Lineage.downstream_dataset_id == Dataset.id)
            .filter(Lineage.upstream_dataset_id == ds.id)
            .all()
        )

        response.append({
            "fqn": ds.fqn,
            "connection": ds.connection_name,
            "database": ds.database_name,
            "schema": ds.schema_name,
            "table": ds.table_name,
            "source_type": ds.source_type,
            "columns": [{"name": c.name, "type": c.type} for c in columns],
            "upstream": [u.fqn for u in upstream],
            "downstream": [d.fqn for d in downstream]
        })

    return response