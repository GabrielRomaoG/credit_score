from src.service.calculate_models_credit_score_average.calculate_models_credit_score_average import (
    ModelsCreditScoreAverageCalculator,
)


def test_calculate():
    mock_cs1_credit_score = 850
    mock_cs1_model_accuracy = 0.6
    mock_cs2_credit_score = 720
    mock_cs2_model_accuracy = 0.9

    result = ModelsCreditScoreAverageCalculator.calculate(
        mock_cs1_credit_score,
        mock_cs1_model_accuracy,
        mock_cs2_credit_score,
        mock_cs2_model_accuracy,
    )

    expected_result = (
        mock_cs1_credit_score * mock_cs1_model_accuracy
        + mock_cs2_credit_score * mock_cs2_model_accuracy
    ) / (mock_cs1_model_accuracy + mock_cs2_model_accuracy)

    assert expected_result == result
