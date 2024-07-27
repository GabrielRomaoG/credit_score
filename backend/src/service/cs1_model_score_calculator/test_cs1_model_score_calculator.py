import unittest
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO
from src.service.cs1_model_score_calculator.cs1_classification_score_enum import (
    Cs1ClassificationScore,
)
from src.service.cs1_model_score_calculator.cs1_model_score_calculator import (
    Cs1ModelScoreCalculator,
)


class TestCs1ModelScoreCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_predict_dto = Cs1ModelPredictResultDTO(
            low=0.1,
            average=0.2,
            high=0.3,
            logit_components=None,
        )
        self.service = Cs1ModelScoreCalculator

    def test_calculate(self):

        result = self.service.calculate(self.mock_predict_dto)

        expected_result = (
            Cs1ClassificationScore.LOW.value * 0.1
            + Cs1ClassificationScore.AVERAGE.value * 0.2
            + Cs1ClassificationScore.HIGH.value * 0.3
        )

        self.assertEqual(result, expected_result)
