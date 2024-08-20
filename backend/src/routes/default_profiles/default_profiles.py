from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header
from kink import di
from src.dtos.predict_request_dto import Locale
from src.routes.default_profiles.response_schema import (
    DefaultProfilesResponse,
)
from src.service.get_default_profiles.get_default_profiles import DefaultProfilesGetter


router = APIRouter(prefix="/default-profiles", tags=["default-profiles"])


@router.get(
    "/", response_model=DefaultProfilesResponse, summary="Get default profiles."
)
async def get_default_profiles(
    Accept_Language: Annotated[Locale, Header()],
    service: DefaultProfilesGetter = Depends(lambda: di[DefaultProfilesGetter]),
):
    try:
        return service.get(accept_language=Accept_Language)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
