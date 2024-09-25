from pydantic import BaseModel, Field

from src.service.generate_feature_relevance_map.generate_feature_relevance_map import (
    FeatureRelevanceMapGenerator,
)

RELEVANCE_SCORE_RANGE = FeatureRelevanceMapGenerator().RELEVANCE_SCORE_RANGE
MIN_SCORE = RELEVANCE_SCORE_RANGE[0]
MAX_SCORE = RELEVANCE_SCORE_RANGE[-1]


class FeaturesRelevance(BaseModel):
    age: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[-2])
    income: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[1])
    gender: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[1], alias="sex")
    education: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[-2])
    num_bank_accounts: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[-2])
    num_credit_card: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[-2])
    num_of_loan: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[2])
    num_of_delayed_payment: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[-2])
    outstanding_debt: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[0])
    credit_history_age: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[-1])
    total_emi_per_month: int = Field(..., ge=MIN_SCORE, le=MAX_SCORE, examples=[0])


class PredictResponse(BaseModel):
    credit_score: int = Field(..., gt=0, lt=1000, examples=[500])
    features_relevance: FeaturesRelevance = Field(...)
