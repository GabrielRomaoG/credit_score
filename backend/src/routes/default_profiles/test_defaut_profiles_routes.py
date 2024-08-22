import unittest
from fastapi.testclient import TestClient
from kink import di
from src.app import app
from src.ml_models.bootstrap import ml_models_bootstrap_di
from src.routes.default_profiles.response_schema import (
    DefaultProfileByIdResponse,
    DefaultProfilesResponse,
)
from src.service.bootstrap import service_bootstrap_di


class TestPredict(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        ml_models_bootstrap_di()
        service_bootstrap_di()

    def tearDown(self):
        di.clear_cache()

    def test_default_profiles(self):
        mock_headers = {"Accept-Language": "en-US"}
        response = self.client.get("/default-profiles/", headers=mock_headers)
        self.assertEqual(response.status_code, 200)
        DefaultProfilesResponse.model_validate(response.json())

    def test_default_profiles_by_id(self):
        mock_headers = {"Accept-Language": "en-US"}
        response = self.client.get("/default-profiles/1", headers=mock_headers)
        self.assertEqual(response.status_code, 200)
        DefaultProfileByIdResponse.model_validate(response.json())

    def test_default_profiles_by_id_pt_br(self):
        mock_headers = {"Accept-Language": "pt-BR"}
        response = self.client.get("/default-profiles/1", headers=mock_headers)
        self.assertEqual(response.status_code, 200)
        DefaultProfileByIdResponse.model_validate(response.json())

    def test_default_profiles_by_id_locale_error(self):
        mock_headers = {"Accept-Language": "es-ES"}
        response = self.client.get("/default-profiles/1", headers=mock_headers)
        self.assertEqual(response.status_code, 422)

    def test_default_profiles_by_id_not_found(self):
        mock_headers = {"Accept-Language": "en-US"}
        response = self.client.get("/default-profiles/100", headers=mock_headers)
        self.assertEqual(response.status_code, 404)

    def test_default_profiles_input_validation_error(self):
        mock_headers = {"Accept-Language": "en-US"}
        response = self.client.get("/default-profiles/abc", headers=mock_headers)
        self.assertEqual(response.status_code, 422)
