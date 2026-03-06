from pydantic import BaseModel


class LineageCreate(BaseModel):
    upstream_dataset: str
    downstream_dataset: str
