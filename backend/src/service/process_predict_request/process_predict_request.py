from logging import Logger, getLogger
from kink import inject
from src.dtos.cs1_model_predict_dto import Cs1ModelPredictResultDTO
from src.dtos.cs2_model_predict_dto import Cs2ModelPredictResultDTO
from src.service.aggregate_models_credit_score.aggregate_models_credit_score import (
    ModelsCreditScoreAggregator,
)
from src.service.generate_feature_relevance_map.generate_feature_relevance_map import (
    FeatureRelevanceMapGenerator,
)

log: Logger = getLogger(__name__)


@inject
class PredictRequestProcessor:
    """
    Class to process the predict request.
    """

    def __init__(
        self,
        aggregate_models_credit_score_service: ModelsCreditScoreAggregator,
        generate_feature_relevance_map_service: FeatureRelevanceMapGenerator,
    ) -> None:
        self._aggregate_models_credit_score_service = (
            aggregate_models_credit_score_service
        )
        self._generate_feature_relevance_map_service = (
            generate_feature_relevance_map_service
        )

    def process(
        self,
        cs1_predict_result: Cs1ModelPredictResultDTO,
        cs1_model_accuracy: float,
        cs2_predict_result: Cs2ModelPredictResultDTO,
        cs2_model_accuracy: float,
    ) -> dict:
        """
        Process the predict request by aggregating the credit scores from two models and generating a feature relevance map.

        Args:
            cs1_predict_result (Cs1ModelPredictResultDTO): The prediction result from the first model.
            cs1_model_accuracy (float): The accuracy of the first model.
            cs2_predict_result (Cs2ModelPredictResultDTO): The prediction result from the second model.
            cs2_model_accuracy (float): The accuracy of the second model.

        Returns:
            dict: A dictionary containing the credit score and the feature relevance map.
                - credit_score (float): The aggregated credit score.
                - features_relevance (dict): The feature relevance map.

        """

        try:

            credit_score = self._aggregate_models_credit_score_service.aggregate(
                cs1_predict_result,
                cs1_model_accuracy,
                cs2_predict_result,
                cs2_model_accuracy,
            )

            feature_relevance_map = (
                self._generate_feature_relevance_map_service.generate(
                    cs1_predict_result.logit_components,
                    cs2_predict_result.logit_components,
                )
            )

            return {
                "credit_score": credit_score,
                "features_relevance": feature_relevance_map,
            }
        except Exception as e:
            log.error("Failed to process predict request: %s", e)
            raise e
