from unittest.mock import MagicMock
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO
from src.dtos.cs2_model_predict_dto import Cs2ModelPredictResultDTO
from src.service.aggregate_models_credit_score.aggregate_models_credit_score import (
    ModelsCreditScoreAggregator,
)
import unittest


class TestModelsCreditScoreAggregator(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_cs1_credit_score_calculator = MagicMock()
        self.mock_cs2_credit_score_calculator = MagicMock()
        self.service = ModelsCreditScoreAggregator(
            cs1_score_calculator=self.mock_cs1_credit_score_calculator,
            cs2_score_calculator=self.mock_cs2_credit_score_calculator,
        )

    def test_aggregate(self):
        mock_cs1_predict_result_dto = Cs1ModelPredictResultDTO(
            low=0.5, average=0.3, high=0.2, logit_components=None
        )
        mock_cs2_predict_result_dto = Cs2ModelPredictResultDTO(
            poor=0.5, standard=0.3, good=0.2, logit_components=None
        )
        mock_cs1_model_accuracy = 0.5
        mock_cs2_model_accuracy = 0.9

        mock_cs1_credit_score = 720
        mock_cs2_credit_score = 800

        self.mock_cs1_credit_score_calculator.calculate.return_value = (
            mock_cs1_credit_score
        )
        self.mock_cs2_credit_score_calculator.calculate.return_value = (
            mock_cs2_credit_score
        )

        result = self.service.aggregate(
            mock_cs1_predict_result_dto,
            mock_cs1_model_accuracy,
            mock_cs2_predict_result_dto,
            mock_cs2_model_accuracy,
        )

        expected_result = (
            mock_cs1_credit_score * mock_cs1_model_accuracy
            + mock_cs2_credit_score * mock_cs2_model_accuracy
        ) / (mock_cs1_model_accuracy + mock_cs2_model_accuracy)

        self.mock_cs1_credit_score_calculator.calculate.assert_called_once_with(
            mock_cs1_predict_result_dto
        )
        self.mock_cs2_credit_score_calculator.calculate.assert_called_once_with(
            mock_cs2_predict_result_dto
        )

        self.assertEqual(expected_result, result)
