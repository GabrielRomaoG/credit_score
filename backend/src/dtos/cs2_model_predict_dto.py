from dataclasses import dataclass


@dataclass
class Cs2LogitComponents:
    """The logit components for each feature. The component is the multiplication of the coefficient and the feature value."""

    num_bank_accounts: float
    num_credit_card: float
    num_of_loan: float
    num_of_delayed_payment: float
    outstanding_debt: float
    credit_history_age: float
    total_emi_per_month: float


@dataclass
class Cs2ModelPredictResultDTO:
    """A dataclass containing the predicted class labels and their corresponding probabilities for the Cs2Model."""

    poor: float
    standard: float
    good: float
    logit_components: Cs2LogitComponents
