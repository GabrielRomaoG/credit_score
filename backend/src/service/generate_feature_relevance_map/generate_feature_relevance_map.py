from logging import Logger, getLogger
from typing import Literal
import numpy as np
from src.dtos.cs1_model_predict_dto import Cs1LogitComponents
from src.dtos.cs2_model_predict_dto import Cs2LogitComponents

log: Logger = getLogger(__name__)


class FeatureRelevanceMapGenerator:
    """
    A class to generate a feature relevance map.
    """

    @classmethod
    def generate(
        cls,
        cs1_logit_components: Cs1LogitComponents,
        cs2_logit_components: Cs2LogitComponents,
    ) -> dict[str, int]:
        """
        Generate a feature relevance map.

        Parameters:
            cs1_logit_components (Cs1LogitComponents): The logit components for the Cs1Model.
            cs2_logit_components (Cs2LogitComponents): The logit components for the Cs2Model.

        Returns:
            Dict[str, float]: The feature relevance map.
        """
        try:
            features_dict = {
                **vars(cs1_logit_components),
                **vars(cs2_logit_components),
            }

            absolute_values = np.abs(list(features_dict.values()))
            mean_value = np.mean(absolute_values)

            relevance_scores = {
                key: cls._calculate_relevance(value, mean_value)
                for key, value in features_dict.items()
            }
            return relevance_scores
        except Exception as e:
            log.error("Failed to generate feature relevance map: %s", e)
            raise e

    @staticmethod
    def _calculate_relevance(
        logit_component_value: float, mean_value: float
    ) -> Literal[range(-2, 3)]:
        abs_value = abs(logit_component_value)
        if abs_value > mean_value:
            score = 2
        elif abs_value <= mean_value and abs_value > mean_value * 0.1:
            score = 1
        elif abs_value <= mean_value * 0.1:
            score = 0
        return -score if logit_component_value < 0 else score
