from dataclasses import dataclass


@dataclass
class Cs2LogitComponents:
    """The logit components for each feature. The component is the multiplication of the coefficient and the feature value."""

    num_bank_accounts: float = 0
    num_credit_card: float = 0
    num_of_loan: float = 0
    num_of_delayed_payment: float = 0
    outstanding_debt: float = 0
    credit_history_age: float = 0
    total_emi_per_month: float = 0


@dataclass
class Cs2ModelPredictResultDTO:
    """A dataclass containing the predicted class labels and their corresponding probabilities for the Cs2Model."""

    poor: float
    standard: float
    good: float
    logit_components: Cs2LogitComponents
