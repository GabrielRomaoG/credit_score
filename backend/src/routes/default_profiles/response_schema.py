from typing import List
from pydantic import BaseModel, Field
from src.dtos.predict_request_dto import PredictRequestDTO
from src.routes.predict.response_schema import PredictResponse


class ProfileInfo(BaseModel):
    profile_id: int = Field(
        ..., ge=0, description="The unique identifier of the profile", examples=[0]
    )
    title: str = Field(
        ..., description="The title of the profile", examples=["young student"]
    )


class DefaultProfilesResponse(BaseModel):
    profiles: List[ProfileInfo] = Field(
        ...,
        description="A list of profile IDs and titles",
        examples=[
            [
                {"profile_id": 0, "title": "young student"},
                {"profile_id": 1, "title": "middle-aged worker"},
            ]
        ],
    )


class DefaultProfileByIdResponse(BaseModel):
    profile_info: ProfileInfo = Field(...)
    predict_input: PredictRequestDTO = Field(...)
    predict_output: PredictResponse = Field(...)
