from random import uniform
from unittest.mock import MagicMock
import numpy as np
from typing import Dict
import unittest
import warnings
import pandas as pd
from sklearn.exceptions import InconsistentVersionWarning
from sklearn.pipeline import Pipeline
from src.dtos.cs2_model_predict_dto import Cs2ModelPredictResultDTO
from src.ml_models.credit_score_2.cs2_model import Cs2Model
from src.dtos.predict_request_dto import (
    Education,
    Features,
    Gender,
)
from src.ml_models.exceptions import ModelNotLoaded


class MockCs1Model(Cs2Model):
    def __init__(self):
        super().__init__()
        self.load = MagicMock()
        self.estimator = MagicMock()
        self.features_names_in = np.array(
            [
                "num_bank_accounts",
                "num_credit_card",
                "num_of_loan",
                "num_of_delayed_payment",
                "outstanding_debt",
                "credit_history_age",
                "total_emi_per_month",
            ]
        )

        self.features_names_out = np.array(
            [
                "num_bank_accounts",
                "num_credit_card",
                "num_of_loan",
                "num_of_delayed_payment",
                "outstanding_debt",
                "credit_history_age",
                "total_emi_per_month",
            ]
        )

        self.classes = np.array(["poor", "standard", "good"])


class TestCs2Model(unittest.TestCase):
    def setUp(self) -> None:
        self.model = Cs2Model()
        self.mock_model = MockCs1Model()

    def test_warning_inconsistent_version(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            loaded_model = self.model.load()  # noqa: F841

            for warning in w:
                if issubclass(warning.category, InconsistentVersionWarning):
                    self.fail(
                        f"InconsistentVersionWarning appeared, this is probably because Sklearn's backend version is different from the one that built the models (ml_scripts_eda). Make sure that the version is the same by putting the same version in both dependencies: \n{warning.message}"
                    )
                    break

    def test_load(self):
        self.model.load()
        self.assertIsInstance(self.model._Cs2Model__raw_model, Dict)
        self.assertEqual(
            list(self.model._Cs2Model__raw_model.keys()),
            ["fit_time", "score_time", "estimator", "test_score", "logreg_model"],
        )
        self.assertIsInstance(self.model, Cs2Model)
        self.assertIsInstance(self.model.estimator, Pipeline)
        self.assertGreater(self.model.accuracy, 0.0)
        self.assertIsInstance(self.model.classes, np.ndarray)
        self.assertEqual(set(self.model.classes), set(["poor", "standard", "good"]))
        self.assertIsInstance(self.model.coefficients, np.ndarray)
        self.assertIsInstance(self.model.features_names_in, np.ndarray)
        self.assertEqual(
            set(self.model.features_names_in),
            set(
                [
                    "num_bank_accounts",
                    "num_credit_card",
                    "num_of_loan",
                    "num_of_delayed_payment",
                    "outstanding_debt",
                    "credit_history_age",
                    "total_emi_per_month",
                ]
            ),
        )
        self.assertEqual(
            set(self.model.features_names_out),
            set(
                [
                    "num_bank_accounts",
                    "num_credit_card",
                    "num_of_loan",
                    "num_of_delayed_payment",
                    "outstanding_debt",
                    "credit_history_age",
                    "total_emi_per_month",
                ]
            ),
        )

    def test_predict_error_model_not_loaded(self):
        mock_dto_features = Features(
            age=30,
            income=10000,
            gender=Gender.FEMALE,
            education=Education.BACHELORS_DEGREE,
            num_bank_accounts=1,
            num_credit_card=1,
            num_of_loan=1,
            num_of_delayed_payment=1,
            outstanding_debt=1000,
            credit_history_age=1,
            total_emi_per_month=1000,
        )
        with self.assertRaises(ModelNotLoaded):
            self.model.predict(mock_dto_features)

    def test_predict(self):
        mock_dto_features = Features(
            age=30,
            income=10000,
            gender=Gender.FEMALE,
            education=Education.BACHELORS_DEGREE,
            num_bank_accounts=1,
            num_credit_card=1,
            num_of_loan=1,
            num_of_delayed_payment=1,
            outstanding_debt=1000,
            credit_history_age=1,
            total_emi_per_month=1000,
        )

        self.mock_model.load.return_value = None
        self.mock_model.estimator.predict_proba.return_value = np.array(
            [[0.0, 0.9, 0.1]]
        )

        n_features = len(self.mock_model.features_names_out)
        n_classes = len(self.mock_model.classes)

        mock_coeffs = [
            [uniform(-3.0, 3.0) for _ in range(n_features)] for _ in range(n_classes)
        ]
        self.mock_model.coefficients = np.array(mock_coeffs)

        result = self.mock_model.predict(mock_dto_features)

        self.assertIsInstance(result, Cs2ModelPredictResultDTO)

        logit_components_dict = vars(result.logit_components)

        for feature, value in logit_components_dict.items():
            mock_feature_value = getattr(mock_dto_features, feature)
            mock_model_feature_value = (
                mock_feature_value
                if isinstance(mock_feature_value, (int, float))
                else 1
            )

            self.assertEqual(
                value,
                mock_coeffs[1][
                    self.mock_model.features_names_out.tolist().index(feature)
                ]
                * mock_model_feature_value,
            )
        self.assertEqual(result.poor, 0.0)
        self.assertEqual(result.standard, 0.9)
        self.assertEqual(result.good, 0.1)

    def test_dto_to_feature_df(self):
        mock_dto_features = Features(
            age=30,
            income=10000,
            gender=Gender.MALE,
            education=Education.BACHELORS_DEGREE,
            num_bank_accounts=1,
            num_credit_card=1,
            num_of_loan=1,
            num_of_delayed_payment=1,
            outstanding_debt=1000,
            credit_history_age=1,
            total_emi_per_month=1000,
        )

        result = self.model._dto_features_to_feature_df(mock_dto_features)

        expected_result = pd.DataFrame(
            {
                "num_bank_accounts": [1],
                "num_credit_card": [1],
                "num_of_loan": [1],
                "num_of_delayed_payment": [1],
                "outstanding_debt": [1000],
                "credit_history_age": [1],
                "total_emi_per_month": [1000],
            }
        )

        pd.testing.assert_frame_equal(result, expected_result)
