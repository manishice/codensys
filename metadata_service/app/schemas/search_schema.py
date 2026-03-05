from pydantic import BaseModel


class SearchResponse(BaseModel):
    fqn: str
    source_type: str