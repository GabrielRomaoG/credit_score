import unittest
from fastapi.testclient import TestClient
from kink import di
from src.app import app
from src.ml_models.bootstrap import ml_models_bootstrap_di
from src.routes.predict.response_schema import PredictResponse
from src.service.bootstrap import service_bootstrap_di


class TestPredict(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        ml_models_bootstrap_di()
        service_bootstrap_di()

    def tearDown(self):
        di.clear_cache()

    def test_predict(self):
        mock_body = {
            "locale": "en-US",
            "features": {
                "age": 30,
                "monthly_income": 10000,
                "sex": "female",
                "education": "bachelors_degree",
                "num_bank_accounts": 1,
                "num_credit_card": 1,
                "num_of_loan": 1,
                "num_of_delayed_payment": 1,
                "outstanding_debt": 1000,
                "credit_history_age": 1,
                "total_emi_per_month": 1000,
            },
        }
        response = self.client.post("/predict/", json=mock_body)
        self.assertEqual(response.status_code, 200)
        PredictResponse.model_validate(response.json())
