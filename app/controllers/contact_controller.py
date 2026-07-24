from fastapi import APIRouter, Request

from app.schemas.contact import ContactRequest

from app.core.dependencies import contact_service

router = APIRouter(tags=["Contact"])


@router.post("/contact")
async def contact(
    request: Request,
    body: ContactRequest,
):

    return await contact_service.process(
        body,
        request.client.host,
    )