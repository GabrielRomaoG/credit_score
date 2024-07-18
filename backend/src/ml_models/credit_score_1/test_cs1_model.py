from numpy import ndarray
from typing import Dict
import unittest
import warnings
import pandas as pd
from sklearn.exceptions import InconsistentVersionWarning
from sklearn.pipeline import Pipeline
from src.ml_models.credit_score_1.cs1_model import Cs1Model
from src.dtos.predict_request_dto import (
    Education,
    Features,
    Gender,
    Locale,
    PredictRequestDTO,
)
from src.ml_models.exceptions import ModelNotLoaded


class TestCs1Model(unittest.TestCase):
    def setUp(self) -> None:
        self.model = Cs1Model()

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
        self.assertIsInstance(self.model.classes, ndarray)
        self.assertIsInstance(self.model.coefficients, ndarray)
        self.assertIsInstance(self.model.features_names, ndarray)

    def test_run_error_model_not_loaded(self):
        mock_dto = PredictRequestDTO(
            locale=Locale.EN_US,
            features=Features(
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
            ),
        )
        with self.assertRaises(ModelNotLoaded) as context:
            self.model.run(mock_dto)

        self.assertEqual(
            str(context.exception),
            "The cs1_model is not loaded, use the load() method first.",
        )

    def test_run(self):
        mock_dto = PredictRequestDTO(
            locale=Locale.EN_US,
            features=Features(
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
            ),
        )

        self.model.load()

        result = self.model.run(mock_dto)

        self.assertIsInstance(result, dict)
        self.assertEqual(set(result.keys()), set(self.model.classes))
        self.assertEqual(len(result), len(self.model.classes))

        for value in result.values():
            self.assertIsInstance(value, float)

    def test___dto_to_feature_df(self):
        mock_dto = PredictRequestDTO(
            locale=Locale.EN_US,
            features=Features(
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
            ),
        )

        result = self.model._Cs1Model__dto_to_feature_df(mock_dto)

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
                "home_ownership": ["owned"],
                "number_of_children": [0],
                "marital_status": ["single"],
            }
        )

        pd.testing.assert_frame_equal(result, expected_result)

    def test__convert_monthly_income_to_annual_income(self):
        mock_value = 10000

        result = self.model._Cs1Model__convert_monthly_income_to_annual_income(
            mock_value
        )

        self.assertEqual(result, 120000)
