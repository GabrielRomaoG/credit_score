import unittest
from unittest.mock import MagicMock, call
from src.dtos.cs1_model_predict_dto import Cs1LogitComponents, Cs1ModelPredictResultDTO
from src.dtos.cs2_model_predict_dto import Cs2LogitComponents, Cs2ModelPredictResultDTO
from src.dtos.features_dto import (
    Education,
    Gender,
    Locale,
    FeaturesDTO,
)
from src.service.process_predict_request.process_predict_request import (
    PredictRequestProcessor,
)
from copyingmock import CopyingMock


class TestPredictRequestProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_cs1_model = CopyingMock()
        self.mock_cs2_model = CopyingMock()
        self.mock_aggregate_models_score_service = MagicMock()
        self.mock_generate_feature_relevance_map_service = MagicMock()
        self.mock_brl_income_to_usd_converter = MagicMock()
        self.service = PredictRequestProcessor(
            cs1_model=self.mock_cs1_model,
            cs2_model=self.mock_cs2_model,
            aggregate_models_credit_score_service=(
                self.mock_aggregate_models_score_service
            ),
            generate_feature_relevance_map_service=(
                self.mock_generate_feature_relevance_map_service
            ),
            convert_brl_income_to_usd_service=self.mock_brl_income_to_usd_converter,
        )

    def test_process(self):
        mock_accept_language = Locale.EN_US
        mock_features_dto = FeaturesDTO(
            age=30,
            monthly_income=10000,
            sex=Gender.FEMALE,
            education=Education.BACHELORS_DEGREE,
            num_bank_accounts=1,
            num_credit_card=1,
            num_of_loan=1,
            num_of_delayed_payment=1,
            outstanding_debt=1000,
            credit_history_age=1,
            total_emi_per_month=1000,
        )

        self.mock_cs1_model.predict.return_value = Cs1ModelPredictResultDTO(
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
        self.mock_cs1_model.accuracy = 0.5

        self.mock_cs2_model.predict.return_value = Cs2ModelPredictResultDTO(
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

        self.mock_cs2_model.accuracy = 0.6

        self.mock_aggregate_models_score_service.aggregate.return_value = 680

        self.mock_generate_feature_relevance_map_service.generate.return_value = {
            "age": -2,
            "income": 1,
        }

        result = self.service.process(
            features_dto=mock_features_dto,
            Accept_Language=mock_accept_language,
        )

        self.mock_cs1_model.predict.assert_called_once_with(mock_features_dto)
        self.mock_cs2_model.predict.assert_called_once_with(mock_features_dto)

        self.mock_aggregate_models_score_service.aggregate.assert_called_once_with(
            self.mock_cs1_model.predict(),
            self.mock_cs1_model.accuracy,
            self.mock_cs2_model.predict(),
            self.mock_cs2_model.accuracy,
        )

        self.mock_generate_feature_relevance_map_service.generate.assert_called_once_with(
            self.mock_cs1_model.predict().logit_components,
            self.mock_cs2_model.predict().logit_components,
        )

        self.assertIsInstance(result, dict)
        self.assertDictEqual(
            result,
            {"credit_score": 680, "features_relevance": {"age": -2, "income": 1}},
        )

    def test_process_locale_pt_br(self):
        mock_accept_language = Locale.PT_BR
        mock_features_dto = FeaturesDTO(
            age=30,
            monthly_income=10000,
            sex=Gender.FEMALE,
            education=Education.BACHELORS_DEGREE,
            num_bank_accounts=1,
            num_credit_card=1,
            num_of_loan=1,
            num_of_delayed_payment=1,
            outstanding_debt=1000,
            credit_history_age=1,
            total_emi_per_month=1500,
        )

        expected_calls = [
            call(mock_features_dto.income),
            call(mock_features_dto.outstanding_debt),
            call(mock_features_dto.total_emi_per_month),
        ]

        self.mock_brl_income_to_usd_converter.calculate_equivalent_usd_income.side_effect = [
            24000,
            12000,
            1500,
        ]

        result = self.service.process(
            features_dto=mock_features_dto,
            Accept_Language=mock_accept_language,
        )

        self.mock_brl_income_to_usd_converter.calculate_equivalent_usd_income.has_calls(
            expected_calls, any_order=False
        )
        self.assertEqual(mock_features_dto.income, 24000)
        self.assertEqual(mock_features_dto.outstanding_debt, 12000)
        self.assertEqual(mock_features_dto.total_emi_per_month, 1500)

        self.mock_cs1_model.predict.assert_called_once_with(mock_features_dto)
        self.mock_cs2_model.predict.assert_called_once_with(mock_features_dto)

        self.mock_aggregate_models_score_service.aggregate.assert_called_once_with(
            self.mock_cs1_model.predict(),
            self.mock_cs1_model.accuracy,
            self.mock_cs2_model.predict(),
            self.mock_cs2_model.accuracy,
        )

        self.mock_generate_feature_relevance_map_service.generate.assert_called_once_with(
            self.mock_cs1_model.predict().logit_components,
            self.mock_cs2_model.predict().logit_components,
        )

        self.assertIsInstance(result, dict)
        self.assertDictEqual(
            result,
            {
                "credit_score": self.mock_aggregate_models_score_service.aggregate(),
                "features_relevance": self.mock_generate_feature_relevance_map_service.generate(),
            },
        )
