from kink import di

from src.ml_models.credit_score_1.cs1_model import Cs1Model
from src.ml_models.credit_score_2.cs2_model import Cs2Model


def ml_models_bootstrap_di() -> None:
    di[Cs1Model] = Cs1Model().load()
    di[Cs2Model] = Cs2Model().load()
