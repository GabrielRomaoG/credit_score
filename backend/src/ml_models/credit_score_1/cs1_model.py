from logging import Logger, getLogger
from os.path import normpath, join, dirname
from typing import Dict
import numpy as np
import pandas as pd
import joblib
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from src.dtos.predict_request_dto import PredictRequestDTO
from src.ml_models.exceptions import ModelNotLoaded

log: Logger = getLogger(__name__)


class Cs1Model:

    def __init__(self) -> None:
        MODEL_FILE_NAME = "cs1_model.z"
        self.model_path: str = normpath(
            join(dirname(__file__), MODEL_FILE_NAME)  # noqa: F821
        )
        self.accuracy: float = 0.0
        self.__raw_model: Dict = None
        self.estimator: Pipeline | BaseEstimator = None
        self.coefficients: np.ndarray = None
        self.features_names: np.ndarray = None

    def load(self) -> None:
        """Loads the ML trained model (plus ancillary files) from file."""
        log.debug("Initializing the model from file %s", self.model_path)
        self.__raw_model = joblib.load(self.model_path)
        self.accuracy = self.__raw_model["test_score"][0]
        self.estimator = self.__raw_model["estimator"][0].best_estimator_
        self.classes = self.estimator.classes_
        self.coefficients = self.estimator.named_steps.logreg.coef_
        self.features_names = self.get_features_names()

        log.debug("cs1_model loaded.")

        return self

    def run(self, dto: PredictRequestDTO) -> Dict:
        """Makes a prediction using the trained ML model."""
        if self.estimator is None:
            raise ModelNotLoaded(
                "the cs1 model is not loaded, use the load() method first."
            )

        data = self.__dto_to_feature_df(dto)
        probs = self.estimator.predict_proba(data).round(3)
        return dict(zip(self.classes, probs[0]))

    def get_features_names(self):
        """
        Get the feature names from the loaded cs1 model.

        Returns:
            The feature names extracted from the model.
        """
        if self.estimator is None:
            raise ModelNotLoaded(
                "the cs1 model is not loaded, use the load() method first."
            )

        mask_features = self.estimator.named_steps["rfe"].get_support()
        cols = self.estimator.named_steps["cols_trans"].get_feature_names_out()

        return cols[mask_features]

    @classmethod
    def __dto_to_feature_df(
        cls,
        predict_request_dto: PredictRequestDTO,
    ) -> pd.DataFrame:
        """
        Converts a PredictRequestDTO to a Pandas DataFrame. The additional columns are due to the model building.
        These columns are not used in the prediction but are necessary for the model to work, thus the placeholder values.

        Args:
            predict_request_dto (PredictRequestDTO): The PredictRequestDTO to convert.

        Returns:
            pd.DataFrame: The converted DataFrame.
        """
        features_data = [predict_request_dto.features.model_dump()]
        features_df = pd.DataFrame(features_data)
        features_df["income"] = features_df["income"].apply(
            cls.__convert_monthly_income_to_annual_income
        )
        features_df["home_ownership"] = ["owned"]
        features_df["number_of_children"] = [0]
        features_df["marital_status"] = ["single"]

        return features_df

    @staticmethod
    def __convert_monthly_income_to_annual_income(monthly_income):
        return monthly_income * 12
