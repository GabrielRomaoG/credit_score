from unittest import TestCase
from src.dtos.cs1_model_predict_dto import Cs1LogitComponents
from src.dtos.cs2_model_predict_dto import Cs2LogitComponents
from src.service.generate_feature_relevance_map.generate_feature_relevance_map import (
    FeatureRelevanceMapGenerator,
)


class TestFeatureRelevanceMapGenerator(TestCase):
    def setUp(self):
        self.service = FeatureRelevanceMapGenerator

    def test_generate(self):
        mock_cs1_logit_components = Cs1LogitComponents(
            age=2.5, income=3.6, gender=-0.7, education=-8.4
        )

        mock_cs2_logit_components = Cs2LogitComponents(
            num_bank_accounts=7.5,
            num_credit_card=3.5,
            num_of_loan=-1.2,
            num_of_delayed_payment=0.32,
            outstanding_debt=-4.7,
            credit_history_age=5.2,
            total_emi_per_month=1.2,
        )

        mock_attributes_list = [
            *vars(mock_cs1_logit_components).keys(),
            *vars(mock_cs2_logit_components).keys(),
        ]

        result = self.service.generate(
            cs1_logit_components=mock_cs1_logit_components,
            cs2_logit_components=mock_cs2_logit_components,
        )

        self.assertIsInstance(result, dict)
        for feature, value in result.items():
            self.assertIn(value, range(-2, 3))
            self.assertIn(feature, mock_attributes_list)

    def test__calculate_relevance_equal_2(self):
        mock_logit_component_value = 200
        mock_mean_value = 100

        result = self.service._calculate_relevance(
            logit_component_value=mock_logit_component_value,
            median_value=mock_mean_value,
        )

        self.assertEqual(result, 2)

    def test__calculate_relevance_equal_1(self):
        mock_logit_component_value = 50
        mock_mean_value = 100

        result = self.service._calculate_relevance(
            logit_component_value=mock_logit_component_value,
            median_value=mock_mean_value,
        )

        self.assertEqual(result, 1)

    def test__calculate_relevance_equal_0(self):
        mock_logit_component_value = 5
        mock_mean_value = 100

        result = self.service._calculate_relevance(
            logit_component_value=mock_logit_component_value,
            median_value=mock_mean_value,
        )

        self.assertEqual(result, 0)

    def test__calculate_relevance_negative_value(self):
        mock_logit_component_value = -200
        mock_mean_value = 100

        result = self.service._calculate_relevance(
            logit_component_value=mock_logit_component_value,
            median_value=mock_mean_value,
        )

        self.assertEqual(result, -2)
