from dataclasses import dataclass


@dataclass
class Cs1LogitComponents:
    """
    The logit components for each feature. The component is the multiplication of the coefficient and the feature value.
    Example:
        age = 30
        coefficient = 0.5
        component = 15
    """

    age: float = 0
    income: float = 0
    gender: float = 0
    education: float = 0


@dataclass
class Cs1ModelPredictResultDTO:
    """
    A dataclass containing the predicted class labels and their corresponding probabilities for the Cs1Model.
    """

    low: float
    average: float
    high: float
    logit_components: Cs1LogitComponents
