import json
import tempfile
import shutil
import unittest
from unittest.mock import MagicMock
from pathlib import Path

from pydantic import ValidationError
from src.dtos.predict_request_dto import Locale
from src.routes.default_profiles.response_schema import DefaultProfileByIdResponse
from src.service.get_default_profiles_by_id.get_default_profiles_by_id import (
    DefaultProfilesByIdGetter,
)


class TestDefaultProfilesByIdGetter(unittest.TestCase):

    def setUp(self):
        self.mock_profiles_getter = MagicMock()
        self.mock_predict_request_processor = MagicMock()
        self.service = DefaultProfilesByIdGetter(
            profiles_getter=self.mock_profiles_getter,
            predict_request_processor=self.mock_predict_request_processor,
        )

    def _create_temp_json_file(self, directory: Path, filename: str, content: dict):
        """Helper function to create a temporary JSON file."""
        file_path = directory / filename
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f)
        return file_path

    def test_get_success(self):
        self.mock_profiles_getter.PROFILES_DIR = Path(tempfile.mkdtemp())

        profile_data = {
            "profile_id": 1,
            "title": "Profile 1",
            "predict_input": {
                "locale": "en-US",
                "features": {
                    "age": 30,
                    "sex": "male",
                    "monthly_income": 75000,
                    "education": "bachelors_degree",
                    "num_bank_accounts": 2,
                    "num_credit_card": 3,
                    "num_of_loan": 2,
                    "num_of_delayed_payment": 2,
                    "outstanding_debt": 10000,
                    "credit_history_age": 12,
                    "total_emi_per_month": 1500,
                },
            },
        }

        locale_dir = self.mock_profiles_getter.PROFILES_DIR / "en-US"
        locale_dir.mkdir(parents=True, exist_ok=True)

        self._create_temp_json_file(
            directory=locale_dir,
            filename="profile_1.json",
            content=profile_data,
        )

        self.mock_predict_request_processor.process.return_value = {
            "credit_score": 750,
            "features_relevance": {
                "age": -2,
                "income": 1,
                "gender": 1,
                "education": -2,
                "num_bank_accounts": -2,
                "num_credit_card": -2,
                "num_of_loan": 2,
                "num_of_delayed_payment": -2,
                "outstanding_debt": 0,
                "credit_history_age": -1,
                "total_emi_per_month": 0,
            },
        }

        result = self.service.get(profile_id=1, accept_language=Locale.EN_US)

        DefaultProfileByIdResponse.model_validate(result)

        self.assertEqual(result["profile_info"]["profile_id"], 1)
        self.assertEqual(result["profile_info"]["title"], "Profile 1")
        self.assertEqual(result["predict_input"], profile_data["predict_input"])
        self.assertIn("predict_output", result)
        self.assertEqual(
            result["predict_output"], self.mock_predict_request_processor.process()
        )

    def test_get_invalid_locale_type(self):
        self.mock_profiles_getter.PROFILES_DIR = Path(tempfile.mkdtemp())

        with self.assertRaises(TypeError) as context:
            self.service.get(profile_id=1, accept_language="invalid_locale")

        self.assertEqual(
            str(context.exception),
            "Invalid type for accept_language: '<class 'str'>'. Must be 'Locale'.",
        )

    def test_get_invalid_profile_id_type(self):
        self.mock_profiles_getter.PROFILES_DIR = Path(tempfile.mkdtemp())

        with self.assertRaises(TypeError) as context:
            self.service.get(profile_id="invalid_id", accept_language=Locale.EN_US)

        self.assertEqual(
            str(context.exception),
            "Invalid type for profile_id: '<class 'str'>'. Must be 'int'.",
        )

    def test_get_directory_not_found(self):
        self.mock_profiles_getter.PROFILES_DIR = Path(tempfile.mkdtemp())

        mock_accept_language = Locale.PT_BR

        with self.assertRaises(FileNotFoundError) as context:
            self.service.get(profile_id=1, accept_language=mock_accept_language)

        self.assertEqual(
            str(context.exception),
            f"Directory for locale '{mock_accept_language.value}' not found.",
        )

    def test_get_profile_not_found(self):
        self.mock_profiles_getter.PROFILES_DIR = Path(tempfile.mkdtemp())
        (self.mock_profiles_getter.PROFILES_DIR / "en-US").mkdir(
            parents=True, exist_ok=True
        )

        with self.assertRaises(FileNotFoundError) as context:
            self.service.get(profile_id=1, accept_language=Locale.EN_US)

        self.assertEqual(
            str(context.exception),
            "Profile with id '1' not found for locale 'en-US'.",
        )

    def test_predict_input_validation_error(self):
        self.mock_profiles_getter.PROFILES_DIR = Path(tempfile.mkdtemp())
        (self.mock_profiles_getter.PROFILES_DIR / "en-US").mkdir(
            parents=True, exist_ok=True
        )

        profile_data = {
            "profile_info": {"profile_id": 1, "title": "Profile 1"},
            "predict_input": {
                "features": {
                    "age": 30,
                    "sex": "male",
                    "monthly_income": 75000,
                    "education": "bachelors_degree",
                    "num_bank_accounts": 2,
                    "num_credit_card": 3,
                    "num_of_loan": 2,
                    "num_of_delayed_payment": 2,
                    "outstanding_debt": 10000,
                    "credit_history_age": 12,
                    "total_emi_per_month": 1500,
                },
            },
        }

        self._create_temp_json_file(
            directory=self.mock_profiles_getter.PROFILES_DIR / "en-US",
            filename="profile_1.json",
            content=profile_data,
        )

        with self.assertRaises(ValidationError):
            self.service.get(profile_id=1, accept_language=Locale.EN_US)

    def tearDown(self):
        shutil.rmtree(self.mock_profiles_getter.PROFILES_DIR)
