from logging import Logger, getLogger
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO
from src.dtos.cs2_model_predict_dto import Cs2ModelPredictResultDTO
from src.service.calculate_cs1_credit_score.calculate_cs1_credit_score import (
    Cs1ModelScoreCalculator,
)
from src.service.calculate_cs2_credit_score.calculate_cs2_credit_score import (
    Cs2ModelScoreCalculator,
)

log: Logger = getLogger(__name__)


class ModelsCreditScoreAggregator:

    def __init__(
        self,
        cs1_score_calculator: Cs1ModelScoreCalculator,
        cs2_score_calculator: Cs2ModelScoreCalculator,
    ) -> None:
        self._cs1_score_calculator = cs1_score_calculator
        self._cs2_score_calculator = cs2_score_calculator

    def aggregate(
        self,
        cs1_predict_result_dto: Cs1ModelPredictResultDTO,
        cs1_model_accuracy: float,
        cs2_predict_result_dto: Cs2ModelPredictResultDTO,
        cs2_model_accuracy: float,
    ) -> int:
        """
        Aggregate the credit scores of CS1 and CS2 models.

        Args:
            cs1_predict_result_dto (Cs1ModelPredictResultDTO): The result of CS1 model prediction.
            cs1_model_accuracy (float): The accuracy of CS1 model.
            cs2_predict_result_dto (Cs2ModelPredictResultDTO): The result of CS2 model prediction.
            cs2_model_accuracy (float): The accuracy of CS2 model.

        Returns:
            int: The average credit score of the models.

        """

        try:
            cs1_credit_score = self._cs1_score_calculator.calculate(
                cs1_predict_result_dto
            )

            cs2_credit_score = self._cs2_score_calculator.calculate(
                cs2_predict_result_dto
            )

            weighted_cs1_score = cs1_credit_score * cs1_model_accuracy
            weighted_cs2_score = cs2_credit_score * cs2_model_accuracy
            total_accuracy = cs1_model_accuracy + cs2_model_accuracy

            weighted_average_score = (
                weighted_cs1_score + weighted_cs2_score
            ) / total_accuracy

            return int(round(weighted_average_score, 0))

        except Exception as e:
            log.error("Failed to aggregate models credit score: %s", e)
            raise e
