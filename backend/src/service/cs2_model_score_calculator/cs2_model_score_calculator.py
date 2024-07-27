from logging import Logger, getLogger
from src.dtos.cs2_model_predict_dto import Cs2ModelPredictResultDTO
from src.service.cs2_model_score_calculator.cs2_classification_score_enum import (
    Cs2ClassificationScore,
)

log: Logger = getLogger(__name__)


class Cs2ModelScoreCalculator:
    """
    Class for calculating the score of a CS2 model.
    """

    @staticmethod
    def calculate(cs2_result_dto: Cs2ModelPredictResultDTO) -> float:
        """
        Calculate the score of the input features using the predicted probabilities of the CS2 model.

        The score is calculated by multiplying the probability of each class with the
        corresponding classification score and summing them up.
        Returns:
            float: The score of the input.
        """
        try:
            score = sum(
                classification.value
                * getattr(cs2_result_dto, classification.name.lower())
                for classification in Cs2ClassificationScore
            )
            return score

        except Exception as e:
            log.error("Failed to calculate score for the Cs2 Model: %s", e)
            raise e
