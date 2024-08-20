from fastapi import APIRouter, Depends
from kink import di
from src.dtos.predict_request_dto import PredictRequestDTO
from src.routes.predict.response_schema import PredictResponse
from src.service.process_predict_request.process_predict_request import (
    PredictRequestProcessor,
)


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post(
    "/", response_model=PredictResponse, summary="Get a credit score prediction."
)
async def get_prediction(
    request: PredictRequestDTO,
    service: PredictRequestProcessor = Depends(lambda: di[PredictRequestProcessor]),
):

    return service.process(request)