import unittest
from src.dtos.cs2_model_predict_dto import Cs2ModelPredictResultDTO
from src.service.cs2_model_score_calculator.cs2_classification_score_enum import (
    Cs2ClassificationScore,
)
from src.service.cs2_model_score_calculator.cs2_model_score_calculator import (
    Cs2ModelScoreCalculator,
)


class TestCs2ModelScoreCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_predict_dto = Cs2ModelPredictResultDTO(
            poor=0.1,
            standard=0.2,
            good=0.3,
            logit_components=None,
        )
        self.service = Cs2ModelScoreCalculator

    def test_calculate(self):

        result = self.service.calculate(self.mock_predict_dto)

        expected_result = (
            Cs2ClassificationScore.POOR.value * 0.1
            + Cs2ClassificationScore.STANDARD.value * 0.2
            + Cs2ClassificationScore.GOOD.value * 0.3
        )

        self.assertEqual(result, expected_result)
