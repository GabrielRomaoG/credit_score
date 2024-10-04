from typing import List
from pydantic import BaseModel, Field
from src.dtos.features_dto import FeaturesDTO
from src.routes.predict.response_schema import PredictResponse


class ProfileInfo(BaseModel):
    profile_id: int = Field(
        ..., ge=0, description="The unique identifier of the profile", examples=[0]
    )
    title: str = Field(
        ..., description="The title of the profile", examples=["young student"]
    )
    img_url: str = Field(
        ...,
        description="The URL of the image associated with the profile",
        examples=["https://example.com/image.png"],
    )


class DefaultProfilesResponse(BaseModel):
    profiles: List[ProfileInfo] = Field(
        ...,
        description="A list of profile IDs and titles",
        examples=[
            [
                {
                    "profile_id": 0,
                    "title": "young student",
                    "img_url": "https://example.com/image.png",
                },
                {
                    "profile_id": 1,
                    "title": "middle-aged worker",
                    "img_url": "https://example.com/image2.png",
                },
            ]
        ],
    )


class DefaultProfileByIdResponse(BaseModel):
    profile_info: ProfileInfo = Field(...)
    features: FeaturesDTO = Field(...)
    predict_output: PredictResponse = Field(...)
