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
    age: int = Field(..., gt=0)
    income: int = Field(..., gt=0)
    gender: Gender
    education: Education
    num_bank_accounts: int = Field(..., gt=0)
    num_credit_card: int = Field(..., gt=0)
    num_of_loan: int = Field(..., gt=0)
    num_of_delayed_payment: int = Field(..., gt=0)
    outstanding_debt: int = Field(..., gt=0)
    credit_history_age: int = Field(..., gt=0)
    total_emi_per_month: int = Field(..., gt=0)


class PredictRequestDTO(BaseModel):
    locale: Locale
    features: Features
