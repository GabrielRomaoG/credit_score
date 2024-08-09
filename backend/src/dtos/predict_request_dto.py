from enum import Enum
from pydantic import BaseModel, Field


class Locale(str, Enum):
    EN_US = "en-US"
    PT_BR = "pt-BR"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class Education(str, Enum):
    BACHELORS_DEGREE = "bachelors_degree"
    MASTERS_DEGREE = "masters_degree"
    DOCTORATE = "doctorate"
    HIGH_SCHOOL_DIPLOMA = "high_school_diploma"
    ASSOCIATES_DEGREE = "associates_degree"


class Features(BaseModel):
    age: int = Field(..., gt=0, examples=[25, 30, 35, 40, 45])
    income: int = Field(..., gt=0, examples=[6000, 7000, 8000, 9000, 10000])
    gender: Gender = Field(..., examples=["male", "female"])
    education: Education = Field(..., examples=["bachelors_degree"])
    num_bank_accounts: int = Field(..., gt=0, examples=[1, 2, 3, 4, 5])
    num_credit_card: int = Field(..., gt=0, examples=[1, 2, 3, 4, 5])
    num_of_loan: int = Field(..., gt=0, examples=[1, 2, 3, 4, 5])
    num_of_delayed_payment: int = Field(..., gt=0, examples=[1, 2, 3, 4, 5])
    outstanding_debt: int = Field(..., gt=0, examples=[1000, 2000, 3000, 4000, 5000])
    credit_history_age: int = Field(..., gt=0, examples=[1, 2, 3, 4, 5])
    total_emi_per_month: int = Field(..., gt=0, examples=[1000, 2000, 3000, 4000, 5000])


class PredictRequestDTO(BaseModel):
    locale: Locale = Field(..., examples=["en-US", "pt-BR"])
    features: Features = Field(...)
