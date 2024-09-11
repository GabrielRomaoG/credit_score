from random import uniform
from unittest.mock import MagicMock
import numpy as np
from typing import Dict
import unittest
import warnings
import pandas as pd
from sklearn.exceptions import InconsistentVersionWarning
from sklearn.pipeline import Pipeline
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO
from src.ml_models.credit_score_1.cs1_model import Cs1Model
from src.dtos.features_dto import (
    Education,
    FeaturesDTO,
    Gender,
)
from src.ml_models.exceptions import ModelNotLoaded


class MockCs1Model(Cs1Model):
    def __init__(self):
        super().__init__()
        self.load = MagicMock()
        self.estimator = MagicMock()
        self.features_names_in = np.array(["gender", "education", "age", "income"])

        self.features_names_out = np.array(
            [
                "gender_female",
                "gender_male",
                "education_associates_degree",
                "education_bachelors_degree",
                "education_doctorate",
                "education_high_school_diploma",
                "education_masters_degree",
                "age",
                "income",
            ]
        )

        self.classes = np.array(["low", "average", "high"])


class TestCs1Model(unittest.TestCase):
    def setUp(self) -> None:
        self.model = Cs1Model()
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
        self.assertIsInstance(self.model._Cs1Model__raw_model, Dict)
        self.assertEqual(
            list(self.model._Cs1Model__raw_model.keys()),
            ["fit_time", "score_time", "estimator", "test_score"],
        )
        self.assertIsInstance(self.model, Cs1Model)
        self.assertIsInstance(self.model.estimator, Pipeline)
        self.assertGreater(self.model.accuracy, 0.0)
        self.assertIsInstance(self.model.classes, np.ndarray)
        self.assertEqual(list(self.model.classes), ["average", "high", "low"])
        self.assertIsInstance(self.model.coefficients, np.ndarray)
        self.assertIsInstance(self.model.features_names_in, np.ndarray)
        self.assertEqual(
            list(self.model.features_names_in), ["gender", "education", "age", "income"]
        )
        self.assertIsInstance(self.model.features_names_out, np.ndarray)
        self.assertEqual(
            list(self.model.features_names_out),
            [
                "gender_female",
                "gender_male",
                "education_associates_degree",
                "education_bachelors_degree",
                "education_doctorate",
                "education_high_school_diploma",
                "education_masters_degree",
                "age",
                "income",
            ],
        )

    def test_predict_error_model_not_loaded(self):
        mock_dto = FeaturesDTO(
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
        with self.assertRaises(ModelNotLoaded):
            self.model.predict(mock_dto)

    def test_predict(self):
        mock_dto_features = FeaturesDTO(
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

        self.mock_model.load.return_value = None
        self.mock_model.estimator.predict_proba.return_value = np.array(
            [[0.0, 0.9, 0.1]]
        )
        mock_coeffs = [[uniform(-3.0, 3.0) for _ in range(9)] for _ in range(3)]
        self.mock_model.coefficients = np.array(mock_coeffs)

        result = self.mock_model.predict(mock_dto_features)

        self.assertIsInstance(result, Cs1ModelPredictResultDTO)
        self.assertEqual(result.logit_components.age, mock_coeffs[1][7] * 30)
        self.assertEqual(result.logit_components.income, mock_coeffs[1][8] * 120000)
        self.assertEqual(result.logit_components.gender, mock_coeffs[1][0])
        self.assertEqual(result.logit_components.education, mock_coeffs[1][3])
        self.assertEqual(result.low, 0.0)
        self.assertEqual(result.average, 0.9)
        self.assertEqual(result.high, 0.1)

    def test_dto_to_feature_df(self):
        mock_dto_features = FeaturesDTO(
            age=30,
            monthly_income=10000,
            sex=Gender.MALE,
            education=Education.BACHELORS_DEGREE,
            num_bank_accounts=1,
            num_credit_card=1,
            num_of_loan=1,
            num_of_delayed_payment=1,
            outstanding_debt=1000,
            credit_history_age=1,
            total_emi_per_month=1000,
        )

        result = self.model._dto_to_feature_df(mock_dto_features)

        expected_result = pd.DataFrame(
            {
                "age": [30],
                "income": [120000],
                "gender": ["male"],
                "education": ["bachelors_degree"],
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

    def test_convert_monthly_income_to_annual_income(self):
        mock_value = 10000

        result = self.model._convert_monthly_to_annual_income(mock_value)

        self.assertEqual(result, 120000)
