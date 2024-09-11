from logging import Logger, getLogger
from kink import inject
from src.dtos.predict_request_dto import Locale, PredictRequestDTO
from src.ml_models.credit_score_1.cs1_model import Cs1Model
from src.ml_models.credit_score_2.cs2_model import Cs2Model
from src.service.aggregate_models_credit_score.aggregate_models_credit_score import (
    ModelsCreditScoreAggregator,
)
from src.service.convert_brl_income_to_usd.convert_brl_income_to_usd import (
    BrlIncomeToUsdConverter,
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
        cs1_model: Cs1Model,
        cs2_model: Cs2Model,
        aggregate_models_credit_score_service: ModelsCreditScoreAggregator,
        generate_feature_relevance_map_service: FeatureRelevanceMapGenerator,
        convert_brl_income_to_usd_service: BrlIncomeToUsdConverter,
    ) -> None:
        self._cs1_model = cs1_model
        self._cs2_model = cs2_model
        self._aggregate_models_credit_score_service = (
            aggregate_models_credit_score_service
        )
        self._generate_feature_relevance_map_service = (
            generate_feature_relevance_map_service
        )
        self._convert_brl_income_to_usd_service = convert_brl_income_to_usd_service

    def process(
        self,
        predict_request_dto: PredictRequestDTO,
        Accept_Language: Locale,
    ) -> dict:
        """
        Process the predict request by aggregating the credit scores from two models
        and generating a feature relevance map.

        Args:
            predict_request_dto (PredictRequestDTO): DTO containing the request data.

        Returns:
            dict: A dictionary containing the credit score and the feature relevance map.
                - credit_score (float): The aggregated credit score.
                - features_relevance (dict): The feature relevance map.

        """

        try:

            if Accept_Language == Locale.PT_BR:
                predict_request_dto.features.income = self._convert_brl_income_to_usd_service.calculate_equivalent_usd_income(
                    predict_request_dto.features.income
                )
                predict_request_dto.features.outstanding_debt = self._convert_brl_income_to_usd_service.calculate_equivalent_usd_income(
                    predict_request_dto.features.outstanding_debt
                )
                predict_request_dto.features.total_emi_per_month = self._convert_brl_income_to_usd_service.calculate_equivalent_usd_income(
                    predict_request_dto.features.total_emi_per_month
                )
            cs1_predict_result = self._cs1_model.predict(predict_request_dto.features)
            cs2_predict_result = self._cs2_model.predict(predict_request_dto.features)

            credit_score = self._aggregate_models_credit_score_service.aggregate(
                cs1_predict_result,
                self._cs1_model.accuracy,
                cs2_predict_result,
                self._cs2_model.accuracy,
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
