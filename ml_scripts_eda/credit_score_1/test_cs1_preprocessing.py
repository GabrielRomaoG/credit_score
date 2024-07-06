import pandas as pd
from credit_score_1.cs1_preprocessing import Cs1DataSetPreProcessing


def test_process():
    mock_df = pd.DataFrame(
        {
            "Age": [25, 40],
            "Gender": ["Female", "Male"],
            "Income": [50000, 100000],
            "Education": ["Bachelor's Degree", "Master's Degree"],
            "Marital Status": ["Married", "Single"],
            "Number of Children": [0, 2],
            "Home Ownership": ["Rented", "Rented"],
            "Credit Score": ["High", "Low"],
        }
    )

    result = Cs1DataSetPreProcessing.process(mock_df)

    expected_result = pd.DataFrame(
        {
            "age": [25, 40],
            "gender": ["female", "male"],
            "income": [50000, 100000],
            "education": ["bachelors_degree", "masters_degree"],
            "marital_status": ["married", "single"],
            "number_of_children": [0, 2],
            "home_ownership": ["rented", "rented"],
            "credit_score": ["high", "low"],
        }
    )

    pd.testing.assert_frame_equal(
        result.sort_index(axis=1),
        expected_result.sort_index(axis=1),
    )
