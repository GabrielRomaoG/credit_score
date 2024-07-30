from logging import Logger, getLogger

log: Logger = getLogger(__name__)


class ModelsCreditScoreAverageCalculator:

    @staticmethod
    def calculate(
        cs1_credit_score: float,
        cs1_model_accuracy: float,
        cs2_credit_score: float,
        cs2_model_accuracy: float,
    ) -> float:
        """
        Calculate the average credit score of the models.

        Args:
            cs1_credit_score (float): The credit score of the CS1 model.
            cs2_credit_score (float): The credit score of the CS2 model.

        Returns:
            float: The average credit score of the models.
        """

        try:
            weighted_cs1_score = cs1_credit_score * cs1_model_accuracy
            weighted_cs2_score = cs2_credit_score * cs2_model_accuracy
            total_accuracy = cs1_model_accuracy + cs2_model_accuracy

            weighted_average_score = (
                weighted_cs1_score + weighted_cs2_score
            ) / total_accuracy

            return weighted_average_score

        except Exception as e:
            log.error("Failed to calculate average credit score: %s", e)
            raise e
