from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryPayloadResponse(SummaryPayloadSchema):
    id: int
