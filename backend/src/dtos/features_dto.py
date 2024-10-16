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


class FeaturesDTO(BaseModel):
    age: int = Field(..., gt=0, examples=[25])
    income: int = Field(..., ge=0, examples=[6000], alias="monthly_income")
    gender: Gender = Field(..., examples=["male"], alias="sex")
    education: Education = Field(..., examples=["bachelors_degree"])
    num_bank_accounts: int = Field(..., ge=0, examples=[1])
    num_credit_card: int = Field(..., ge=0, examples=[2])
    num_of_loan: int = Field(..., ge=0, examples=[3])
    num_of_delayed_payment: int = Field(..., ge=0, examples=[2])
    outstanding_debt: int = Field(..., ge=0, examples=[2000])
    credit_history_age: int = Field(..., ge=0, examples=[3])
    total_emi_per_month: int = Field(..., ge=0, examples=[2000])
