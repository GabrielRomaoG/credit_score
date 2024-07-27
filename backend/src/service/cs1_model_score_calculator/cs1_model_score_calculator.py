from logging import Logger, getLogger
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO
from src.service.cs1_model_score_calculator.cs1_classification_score_enum import (
    Cs1ClassificationScore,
)

log: Logger = getLogger(__name__)


class Cs1ModelScoreCalculator:
    """
    Class for calculating the score of a CS1 model.
    """

    def __init__(self, cs1_result_dto: Cs1ModelPredictResultDTO) -> None:
        """
        Initialize the Cs1ModelScoreCalculator with the result of the prediction made by
        the CS1 model.

        Args:
            cs1_result_dto (Cs1ModelPredictResultDTO): The result of the prediction made by the
                CS1 model. It contains the predicted probabilities of the input features for each
                class.
        """
        self.predict_dto = cs1_result_dto

    def calculate_score(self) -> float:
        """
        Calculate the score of the input features using the predicted probabilities of the CS1 model.

        The score is calculated by multiplying the probability of each class with the
        corresponding classification score and summing them up.
        Returns:
            float: The score of the input.
        """
        try:
            score = 0.0

            for classification in Cs1ClassificationScore:
                probability = getattr(self.predict_dto, classification.name.lower())
                score += classification.value * probability

            return score

        except Exception as e:
            log.error("Failed to calculate score for the Cs1 Model: %s", e)
            raise e
