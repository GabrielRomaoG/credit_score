from kink import di

from src.ml_models.credit_score_1.cs1_model import Cs1Model
from src.ml_models.credit_score_2.cs2_model import Cs2Model
from src.service.aggregate_models_credit_score.aggregate_models_credit_score import (
    ModelsCreditScoreAggregator,
)
from src.service.calculate_cs1_credit_score.calculate_cs1_credit_score import (
    Cs1ModelScoreCalculator,
)
from src.service.calculate_cs2_credit_score.calculate_cs2_credit_score import (
    Cs2ModelScoreCalculator,
)
from src.service.convert_brl_income_to_usd.convert_brl_income_to_usd import (
    BrlIncomeToUsdConverter,
)
from src.service.generate_feature_relevance_map.generate_feature_relevance_map import (
    FeatureRelevanceMapGenerator,
)
from src.service.get_default_profiles.get_default_profiles import DefaultProfilesGetter
from src.service.process_predict_request.process_predict_request import (
    PredictRequestProcessor,
)


def service_bootstrap_di() -> None:
    di[ModelsCreditScoreAggregator] = ModelsCreditScoreAggregator(
        Cs1ModelScoreCalculator,
        Cs2ModelScoreCalculator,
    )

    di[PredictRequestProcessor] = PredictRequestProcessor(
        di[Cs1Model],
        di[Cs2Model],
        di[ModelsCreditScoreAggregator],
        FeatureRelevanceMapGenerator,
        BrlIncomeToUsdConverter(),
    )

    di[DefaultProfilesGetter] = DefaultProfilesGetter()
