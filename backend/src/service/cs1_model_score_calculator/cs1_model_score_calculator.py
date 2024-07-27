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

    @staticmethod
    def calculate(cs1_result_dto: Cs1ModelPredictResultDTO) -> float:
        """
        Calculate the score of the input features using the predicted probabilities of the CS1 model.

        The score is calculated by multiplying each class's probability with its corresponding classification score,
        and then summing these products.

        Args:
            cs1_result_dto (Cs1ModelPredictResultDTO): The result of the prediction made by the CS1 model.

        Returns:
            float: The score of the input features.

        """

        try:
            score = sum(
                classification.value
                * getattr(cs1_result_dto, classification.name.lower())
                for classification in Cs1ClassificationScore
            )
            return score

        except Exception as e:
            log.error("Failed to calculate score for the Cs1 Model: %s", e)
            raise e
