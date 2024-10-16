from logging import Logger, getLogger
from os.path import normpath, join, dirname
from typing import Dict
import numpy as np
import pandas as pd
import joblib
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO, Cs1LogitComponents
from src.dtos.features_dto import FeaturesDTO
from src.ml_models.exceptions import ModelNotLoaded

log: Logger = getLogger(__name__)


class Cs1Model:
    """Class representing the CS1 Model for making predictions."""

    MODEL_FILE_NAME = "cs1_model.z"

    def __init__(self) -> None:
        """Initialize the Cs1Model with default values and paths."""
        self.model_path: str = normpath(join(dirname(__file__), self.MODEL_FILE_NAME))

    def load(self) -> "Cs1Model":
        """
        Load the ML trained model from file.

        Returns:
            Cs1Model: The instance of the loaded Cs1Model.
        """
        log.debug("Initializing the model from file %s", self.model_path)
        try:
            self.__raw_model: Dict = joblib.load(self.model_path)
            self.accuracy: float = self.__raw_model["test_score"][0]
            self.estimator: Pipeline | BaseEstimator = self.__raw_model["estimator"][
                0
            ].best_estimator_
            self.classes: np.ndarray = self.estimator.classes_
            self.coefficients: np.ndarray = self.estimator.named_steps["logreg"].coef_
            self.features_names_in: np.ndarray = self.estimator.feature_names_in_
            self.features_names_out: np.ndarray = (
                self.estimator.named_steps.cols_trans.get_feature_names_out()
            )
            log.debug("cs1_model loaded successfully.")
        except Exception as e:
            log.error("Failed to load cs1_model: %s", e)
            raise ModelNotLoaded(e)

        return self

    def predict(self, dto_features: FeaturesDTO) -> Cs1ModelPredictResultDTO:
        """
        Make a prediction using the trained ML model.

        Args:
            dto_features (FeaturesDTO): The input features for prediction.

        Returns:
            Cs1ModelPredictResultDTO: A dataclass containing the predicted class labels and their
                corresponding probabilities.

        Raises:
            ModelNotLoaded: If the model is not loaded.
        """
        try:
            data = self._dto_to_feature_df(dto_features)
            probabilities = self.estimator.predict_proba(data).round(3)[0]
            return Cs1ModelPredictResultDTO(
                low=probabilities[self.classes == "low"][0],
                average=probabilities[self.classes == "average"][0],
                high=probabilities[self.classes == "high"][0],
                logit_components=self._get_logit_components(data, probabilities),
            )
        except AttributeError as e:
            raise ModelNotLoaded(
                f"The cs1_model probably is not loaded, use the load() method first.\nComplete error message: {e} "
            )

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
    ) -> Cs1LogitComponents:
        """
        Get the logit components for each class.

        Returns:
            LogitComponents: A dataclass containing the logit components for each class.
        """
        clf_result_index = np.argmax(probabilities)
        clf_coeffs = self.coefficients[clf_result_index]

        logit_components = Cs1LogitComponents()

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

    @classmethod
    def _dto_to_feature_df(cls, dto_features: FeaturesDTO) -> pd.DataFrame:
        """
        Convert a PredictRequestDTO to a Pandas DataFrame.

        Args:
            dto_features (FeaturesDTO): The data transfer object to convert.

        Returns:
            pd.DataFrame: The converted DataFrame. The DataFrame contains the following columns:
                - age (int): The age of the individual.
                - income (int): The annual income of the individual.
                - gender (str): The gender of the individual.
                - education (str): The education level of the individual.
                - num_bank_accounts (int): The number of bank accounts the individual has.
                - num_credit_card (int): The number of credit cards the individual has.
                - num_of_loan (int): The number of loans the individual has.
                - num_of_delayed_payment (int): The number of times the individual has missed a payment.
                - outstanding_debt (int): The amount of outstanding debt the individual has.
                - credit_history_age (int): The age of the individual's credit history.
                - total_emi_per_month (int): The total EMI (Equated Monthly Installment) paid by the individual per month.
        """
        features_data = [dto_features.model_dump()]
        features_df = pd.DataFrame(features_data)
        features_df["income"] = features_df["income"].apply(
            cls._convert_monthly_to_annual_income
        )
        return features_df

    @staticmethod
    def _convert_monthly_to_annual_income(monthly_income: int) -> int:
        """
        Convert monthly income to annual income.

        Args:
            monthly_income (int): The monthly income.

        Returns:
            int: The annual income.
        """
        return monthly_income * 12
