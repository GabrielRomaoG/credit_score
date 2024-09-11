from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header
from kink import di
from src.dtos.features_dto import Locale
from src.routes.default_profiles.response_schema import (
    DefaultProfileByIdResponse,
    DefaultProfilesResponse,
)
from src.service.get_default_profiles.get_default_profiles import DefaultProfilesGetter
from src.service.get_default_profiles_by_id.get_default_profiles_by_id import (
    DefaultProfilesByIdGetter,
)


router = APIRouter(prefix="/default-profiles", tags=["default-profiles"])


@router.get(
    "/", response_model=DefaultProfilesResponse, summary="Get default profiles."
)
async def get_default_profiles(
    Accept_Language: Annotated[Locale, Header()],
    service: DefaultProfilesGetter = Depends(lambda: di[DefaultProfilesGetter]),
) -> DefaultProfilesResponse:
    """
    Retrieves a list of default profiles for the given locale.

    Args:
        accept_language (str): The locale specifying which profiles to retrieve.
            Should be in the format of ISO 639-1 language code and ISO 3166-1 alpha-2
            country code separated by a hyphen (e.g. en-US).

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing profile_id and title.
    """
    try:
        return service.get(accept_language=Accept_Language)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/{profile_id}",
    response_model=DefaultProfileByIdResponse,
    summary="Get default profile by id.",
)
async def get_default_profile_by_id(
    profile_id: int,
    Accept_Language: Annotated[Locale, Header()],
    service: DefaultProfilesByIdGetter = Depends(lambda: di[DefaultProfilesByIdGetter]),
):
    try:
        return service.get(profile_id=profile_id, accept_language=Accept_Language)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
