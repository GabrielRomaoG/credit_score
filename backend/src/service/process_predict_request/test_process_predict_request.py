import unittest
from unittest.mock import MagicMock
from src.dtos.cs1_model_predict_dto import Cs1LogitComponents, Cs1ModelPredictResultDTO
from src.dtos.cs2_model_predict_dto import Cs2LogitComponents, Cs2ModelPredictResultDTO
from src.service.process_predict_request.process_predict_request import (
    PredictRequestProcessor,
)


class TestPredictRequestProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_aggregate_models_score_service = MagicMock()
        self.mock_generate_feature_relevance_map_service = MagicMock()
        self.service = PredictRequestProcessor(
            aggregate_models_credit_score_service=(
                self.mock_aggregate_models_score_service
            ),
            generate_feature_relevance_map_service=(
                self.mock_generate_feature_relevance_map_service
            ),
        )

    def test_process(self):
        mock_cs1_predict_result = Cs1ModelPredictResultDTO(
            low=0.1,
            average=0.2,
            high=0.3,
            logit_components=Cs1LogitComponents(
                age=0.1,
                income=0.2,
                gender=0.3,
                education=0.4,
            ),
        )
        mock_cs1_model_accuracy = 0.5

        mock_cs2_predict_result = Cs2ModelPredictResultDTO(
            poor=0.1,
            standard=0.2,
            good=0.3,
            logit_components=Cs2LogitComponents(
                num_bank_accounts=0.1,
                num_credit_card=0.2,
                num_of_loan=0.3,
                num_of_delayed_payment=0.4,
                outstanding_debt=0.5,
                credit_history_age=0.6,
                total_emi_per_month=0.7,
            ),
        )

        mock_cs2_model_accuracy = 0.6

        self.mock_aggregate_models_score_service.aggregate.return_value = 680

        self.mock_generate_feature_relevance_map_service.generate.return_value = {
            "age": -2,
            "income": 1,
        }

        result = self.service.process(
            mock_cs1_predict_result,
            mock_cs1_model_accuracy,
            mock_cs2_predict_result,
            mock_cs2_model_accuracy,
        )

        self.mock_aggregate_models_score_service.aggregate.assert_called_once_with(
            mock_cs1_predict_result,
            mock_cs1_model_accuracy,
            mock_cs2_predict_result,
            mock_cs2_model_accuracy,
        )

        self.mock_generate_feature_relevance_map_service.generate.assert_called_once_with(
            mock_cs1_predict_result.logit_components,
            mock_cs2_predict_result.logit_components,
        )

        self.assertIsInstance(result, dict)
        self.assertDictEqual(
            result,
            {"credit_score": 680, "features_relevance": {"age": -2, "income": 1}},
        )
