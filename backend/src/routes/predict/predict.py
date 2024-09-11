from typing import Annotated
from fastapi import APIRouter, Depends, Header
from kink import di
from src.dtos.features_dto import Locale, FeaturesDTO
from src.routes.predict.response_schema import PredictResponse
from src.service.process_predict_request.process_predict_request import (
    PredictRequestProcessor,
)


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post(
    "/", response_model=PredictResponse, summary="Get a credit score prediction."
)
async def get_prediction(
    Accept_Language: Annotated[Locale, Header()],
    request: FeaturesDTO,
    service: PredictRequestProcessor = Depends(lambda: di[PredictRequestProcessor]),
):

    return service.process(request, Accept_Language)
