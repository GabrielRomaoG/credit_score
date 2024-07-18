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


class Cs2Model:
    """Class representing the CS1 Model for making predictions."""

    MODEL_FILE_NAME = "cs2_model.z"

    def __init__(self) -> None:
        """Initialize the Cs1Model with default values and paths."""
        self.model_path: str = normpath(join(dirname(__file__), self.MODEL_FILE_NAME))

    def load(self) -> "Cs2Model":
        """
        Load the ML trained model from file.

        Returns:
            Cs1Model: The instance of the loaded Cs1Model.

        Raises:
            ModelNotLoaded: If the model fails to load.
        """
        log.debug("Initializing the model from file %s", self.model_path)
        try:
            self.__raw_model: Dict = joblib.load(self.model_path)
            self.__log_reg = self.__raw_model["logreg_model"]
            self.accuracy: float = self.__raw_model["test_score"][0]
            self.estimator: Pipeline | BaseEstimator = self.__raw_model["estimator"][
                0
            ].best_estimator_
            self.classes: np.ndarray = self.estimator.classes_
            self.coefficients: np.ndarray = self.__log_reg.coef_
            self.features_names: np.ndarray = self.estimator.feature_names_in_
            log.debug("cs2_model loaded successfully.")
        except Exception as e:
            log.error("Failed to load cs2_model: %s", e)
            raise ModelNotLoaded(e)

        return self

    def run(self, dto: PredictRequestDTO) -> Dict[str, float]:
        """
        Make a prediction using the trained ML model.

        Args:
            dto (PredictRequestDTO): The data transfer object containing input features.

        Returns:
            Dict[str, float]: A dictionary mapping class labels to their predicted probabilities.

        Raises:
            ModelNotLoaded: If the model is not loaded.
        """
        try:
            data = self.__dto_to_feature_df(dto)
            probabilities = self.estimator.predict_proba(data).round(3)
            return dict(zip(self.classes, probabilities[0]))
        except AttributeError:
            raise ModelNotLoaded(
                "The cs2_model is not loaded, use the load() method first."
            )

    @staticmethod
    def __dto_to_feature_df(dto: PredictRequestDTO) -> pd.DataFrame:
        """
        Convert a PredictRequestDTO to a Pandas DataFrame. The reason for the column removal is that
        the SGD classifier only accepts the columns that were present in the model fit.

        Args:
            dto (PredictRequestDTO): The data transfer object to convert.

        Returns:
            pd.DataFrame: The converted DataFrame.
        """
        features_data = [dto.features.model_dump()]
        features_df = pd.DataFrame(features_data).drop(
            columns=["age", "income", "gender", "education"]
        )
        return features_df
