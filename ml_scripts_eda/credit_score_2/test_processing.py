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


def test_num_of_delayed_payment():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_of_Delayed_Payment": ["2", "3", "-1_", "24_", NaN],
        }
    )

    result = Cs2DataSetPreProcessing().process_num_of_delayed_payment(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_of_Delayed_Payment": [2.0, 3.0, 0.0, 24.0, 12.0],
        }
    )

    pd.testing.assert_frame_equal(
        result.sort_index(axis=1), expected_result.sort_index(axis=1), check_dtype=False
    )


def test_process_credit_history_age():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Credit_History_Age": [
                "22 years and 1 months",
                "15 years and 10 months",
                "3 years and 7 months",
                "2 years and 11 months",
                NaN,
            ],
        },
    )

    result = Cs2DataSetPreProcessing().process_credit_history_age(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Credit_History_Age": [265.0, 190.0, 43.0, 35.0, 39.0],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)
