from logging import Logger, getLogger
from os.path import normpath, join, dirname
from typing import Dict
import numpy as np
import pandas as pd
import joblib
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from src.dtos.cs2_model_predict_dto import Cs2LogitComponents, Cs2ModelPredictResultDTO
from src.dtos.features_dto import FeaturesDTO
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
            self.features_names_in: np.ndarray = self.estimator.feature_names_in_
            self.features_names_out: np.ndarray = self.estimator.feature_names_in_
            log.debug("cs2_model loaded successfully.")
        except Exception as e:
            log.error("Failed to load cs2_model: %s", e)
            raise ModelNotLoaded(e)

        return self

    def predict(self, dto_features: FeaturesDTO) -> Cs2ModelPredictResultDTO:
        """
        Make a prediction using the trained ML model.

        Args:
            dto_features (FeaturesDTO): The input features for prediction.

        Returns:
            Cs2ModelPredictResultDTO: A dataclass containing the predicted class labels and their
                corresponding probabilities.

        Raises:
            ModelNotLoaded: If the model is not loaded.
        """
        try:
            data = self._dto_features_to_feature_df(dto_features)
            probabilities = self.estimator.predict_proba(data).round(3)[0]
            return Cs2ModelPredictResultDTO(
                poor=probabilities[self.classes == "poor"][0],
                standard=probabilities[self.classes == "standard"][0],
                good=probabilities[self.classes == "good"][0],
                logit_components=self._get_logit_components(data, probabilities),
            )
        except AttributeError as e:
            raise ModelNotLoaded(
                f"The cs2_model is probably not loaded, use the load() method first.\nComplete error message: {e}"
            )

    @staticmethod
    def _dto_features_to_feature_df(dto_features: FeaturesDTO) -> pd.DataFrame:
        """
        Convert a PredictRequestDTO to a Pandas DataFrame. The conversion is done by extracting
        feature values from the DTO and creating a DataFrame with only the features that were present
        in the training data.

        Args:
            dto_features (FeaturesDTO): The data transfer object containing the feature values.

        Returns:
            pd.DataFrame: The converted DataFrame.
        """
        features_data = [dto_features.model_dump()]
        features_df = pd.DataFrame(features_data).drop(
            columns=["age", "income", "gender", "education"]
        )
        return features_df

    def _get_feature_component(
        self, clf_coeffs: np.ndarray, feature_name: str, feature_value: float | int
    ) -> float:
        """
        Helper function to get the component for a specific feature.
        """
        feature_index = np.nonzero(self.features_names_out == feature_name)[0][0]
        return clf_coeffs[feature_index] * feature_value

    def _get_logit_components(
        self, features_df: pd.DataFrame, probabilities: np.ndarray
    ) -> Cs2LogitComponents:
        """
        Get the logit components for each class.

        Returns:
            LogitComponents: A dataclass containing the logit components for each class.
        """
        clf_result_index = np.argmax(probabilities)
        clf_coeffs = self.coefficients[clf_result_index]

        logit_components = Cs2LogitComponents()

        for feature in self.features_names_in:
            value = features_df.at[0, feature]

            if isinstance(value, (np.integer, np.floating)):
                feature_name = feature
                feature_value = value
            else:
                feature_name = f"{feature}_{value.value}"
                feature_value = 1

            setattr(
                logit_components,
                feature,
                self._get_feature_component(clf_coeffs, feature_name, feature_value),
            )

        return logit_components
