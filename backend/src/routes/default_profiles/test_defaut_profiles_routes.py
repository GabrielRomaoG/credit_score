import unittest
from fastapi.testclient import TestClient
from kink import di
from src.app import app
from src.ml_models.bootstrap import ml_models_bootstrap_di
from src.routes.default_profiles.response_schema import DefaultProfilesResponse
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
