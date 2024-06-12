from numpy import NaN
import pandas as pd
from processing import Cs2DataSetPreProcessing


def test_process_age():
    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
            ],
            "Age": [
                "32",
                "33_",
                "8698",
                "33",
                "33",
                "25",
                "25",
                "275",
                "26",
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_age(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
            ],
            "Age": [32, 33, 33, 33, 33, 25, 25, 25, 26],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_occupation():
    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Occupation": [
                "Engineer",
                "Engineer",
                "Engineer_",
                "Doctor",
                "____",
                "Doctor",
            ],
        }
    )
    result = Cs2DataSetPreProcessing.process_occupation(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Occupation": [
                "Engineer",
                "Engineer",
                "Engineer",
                "Doctor",
                "Doctor",
                "Doctor",
            ],
        }
    )

    pd.testing.assert_frame_equal(
        result.sort_index(axis=1), expected_result.sort_index(axis=1), check_dtype=False
    )


def test_process_process_monthly_inhand_salary():
    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Monthly_Inhand_Salary": [
                1000.0,
                NaN,
                3000.0,
                4000.0,
                NaN,
                5000.0,
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_monthly_inhand_salary(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Monthly_Inhand_Salary": [
                1000.0,
                2000.0,
                3000.0,
                4000.0,
                4500.0,
                5000.0,
            ],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_outliers_from_cols():
    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
            ],
            "col1": [40, 40, 9999, 40, 10, 10, 725, 10],
            "col2": [100, 100, 6326, 100, 200, 200, 300, 9999],
        }
    )

    result = Cs2DataSetPreProcessing.process_outliers_from_cols(
        mock_df, ["col1", "col2"]
    )

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
            ],
            "col1": [40, 40, 40, 40, 10, 10, 10, 10],
            "col2": [100, 100, 100, 100, 200, 200, 300, 200],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_num_of_loan():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_of_Loan": ["2", "3", "3600", "-1_", "24_", "24"],
        }
    )

    result = Cs2DataSetPreProcessing.process_num_of_loan(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_of_Loan": [2, 3, 3, 24, 24, 24],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


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


def test_process_num_of_delayed_payment():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_of_Delayed_Payment": ["2", "3", "3600", "-1_", "24_", NaN],
        }
    )

    result = Cs2DataSetPreProcessing().process_num_of_delayed_payment(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_of_Delayed_Payment": [2, 3, 3, 24, 24, 24],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_changed_credit_limit():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Changed_Credit_Limit": ["2.0", "_", "2.0", "-4.0", "-4.0", "_"],
        }
    )

    result = Cs2DataSetPreProcessing.process_changed_credit_limit(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Changed_Credit_Limit": [2.0, 2.0, 2.0, -4.0, -4.0, -4.0],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_num_credit_inquiries():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_Credit_Inquiries": [2.0, 36995, 2.0, 4.0, 4.0, NaN],
        }
    )

    result = Cs2DataSetPreProcessing.process_num_credit_inquiries(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Num_Credit_Inquiries": [2, 2, 2, 4, 4, 4],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_credit_mix():
    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
            ],
            "Credit_Mix": [
                "A",
                "_",
                "A",
                "B",
                "_",
                "_",
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_credit_mix(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3909",
                "CUS_0x3910",
                "CUS_0x3910",
                "CUS_0x3910",
            ],
            "Credit_Mix": [
                "A",
                "A",
                "A",
                "B",
                "B",
                "B",
            ],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


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
                "22 Years and 1 Months",
                "15 Years and 10 Months",
                "2 Years and 11 Months",
                "2 Years and 11 Months",
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
            "Credit_History_Age": [265, 190, 35, 35, 35],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_amount_invested_monthly():

    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Amount_invested_monthly": [
                "100.0",
                "200.0",
                "__10000__",
                "400.0",
                NaN,
                "300.0",
            ],
        },
    )

    result = Cs2DataSetPreProcessing.process_amount_invested_monthly(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Amount_invested_monthly": [
                100.0,
                200.0,
                150.0,
                400.0,
                350.0,
                300.0,
            ],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)


def test_process_monthly_balance():
    mock_df = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Monthly_Balance": [
                "100.0",
                "200.0",
                "__300__",
                "400.0",
                NaN,
                "500.0",
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_monthly_balance(mock_df)

    expected_result = pd.DataFrame(
        {
            "Customer_ID": [
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd40",
                "CUS_0xd41",
                "CUS_0xd41",
                "CUS_0xd41",
            ],
            "Monthly_Balance": [
                100.0,
                200.0,
                150.0,
                400.0,
                450.0,
                500.0,
            ],
        }
    )

    pd.testing.assert_frame_equal(result, expected_result)
