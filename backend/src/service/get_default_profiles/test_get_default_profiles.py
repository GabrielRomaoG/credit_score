import unittest
from pathlib import Path
import tempfile
import shutil
import json
from src.dtos.features_dto import Locale
from src.service.get_default_profiles.get_default_profiles import DefaultProfilesGetter


class TestDefaultProfilesGetter(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.service = DefaultProfilesGetter()

    def _create_temp_json_file(self, directory, filename, content):
        """Helper function to create a temporary JSON file."""
        file_path = Path(directory) / filename
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f)
        return file_path

    def test_get_profiles_success(self):
        locale_dir = Path(self.test_dir) / "en-US"
        locale_dir.mkdir(parents=True, exist_ok=True)

        profile_1 = {"profile_id": 1, "title": "Profile 1"}
        profile_2 = {"profile_id": 2, "title": "Profile 2"}

        self._create_temp_json_file(locale_dir, "profile_1.json", profile_1)
        self._create_temp_json_file(locale_dir, "profile_2.json", profile_2)

        self.service.PROFILES_DIR = Path(self.test_dir)

        result = self.service.get(accept_language=Locale.EN_US)

        self.assertIsInstance(result, dict)
        self.assertIn("profiles", result)

        result_profiles = result["profiles"]

        self.assertIsInstance(result_profiles, list)
        self.assertEqual(len(result_profiles), 2)
        self.assertIn({"profile_id": 1, "title": "Profile 1"}, result_profiles)
        self.assertIn({"profile_id": 2, "title": "Profile 2"}, result_profiles)

    def test_get_profiles_directory_not_found(self):
        self.service.PROFILES_DIR = Path(self.test_dir) / "non_existent_directory"
        mock_accept_language = Locale.PT_BR

        with self.assertRaises(FileNotFoundError) as context:
            self.service.get(accept_language=mock_accept_language)

        self.assertEqual(
            str(context.exception),
            f"Directory for locale '{mock_accept_language.value}' not found.",
        )

    def test_get_accept_language_invalid(self):
        mock_accept_language = "invalid"

        with self.assertRaises(TypeError) as context:
            self.service.get(accept_language=mock_accept_language)

        self.assertEqual(
            str(context.exception),
            "Invalid type for accept_language: '<class 'str'>'. Must be 'Locale'.",
        )

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        self.service.get.cache_clear()
