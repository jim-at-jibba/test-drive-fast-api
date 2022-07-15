from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryPayloadResponse


router = APIRouter()

@router.post("/", response_model=SummaryPayloadResponse, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryPayloadSchema:
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object
