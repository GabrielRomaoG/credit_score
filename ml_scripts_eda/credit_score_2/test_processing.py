from numpy import NaN
import pandas as pd
from processing import Cs2DataSetPreProcessing


def test_process_type_of_loan():

    mock_df = pd.DataFrame(
        {
            "ID": [1, 2, 3],
            "Type_of_Loan": [
                "Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan",
                NaN,
                "Home Equity Loan, Auto Loan, travel Loan, and Auto Loan",
            ],
        }
    )
    result = Cs2DataSetPreProcessing().process_type_of_loan(mock_df)

    print(result)

    expected_result = pd.DataFrame(
        {
            "ID": [1, 2, 3],
            "type_of_loan_Auto Loan": [1, 0, 1],
            "type_of_loan_Credit-Builder Loan": [1, 0, 0],
            "type_of_loan_Personal Loan": [1, 0, 0],
            "type_of_loan_Home Equity Loan": [1, 0, 1],
            "type_of_loan_travel Loan": [0, 0, 1],
        }
    )

    pd.testing.assert_frame_equal(
        result.sort_index(axis=1), expected_result.sort_index(axis=1), check_dtype=False
    )
