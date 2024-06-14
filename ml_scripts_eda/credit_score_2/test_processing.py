from numpy import NaN
import pandas as pd
from processing import Cs2DataSetPreProcessing

# 0x163a5
# 0x23922
# 0xfd6e


def test_process():
    mock_df = pd.DataFrame(
        {
            "ID": {0: "0xfd6e", 1: "0x163a5", 2: "0x23922"},
            "Customer_ID": {
                0: "CUS_0x3dd8",
                1: "CUS_0x2bdc",
                2: "CUS_0x24bc",
            },
            "Month": {0: "January", 1: "August", 2: "January"},
            "Name": {
                0: "Anirban Nagy",
                1: "Greg Roumeliotisp",
                2: "Chuck Mikolajczakb",
            },
            "Age": {0: "24", 1: "29", 2: "48"},
            "SSN": {0: "851-44-4923", 1: "454-30-4171", 2: "664-52-6558"},
            "Occupation": {0: "Entrepreneur", 1: "Writer", 2: "Engineer"},
            "Annual_Income": {
                0: "32928.14",
                1: "119223.09",
                2: "116224.68",
            },
            "Monthly_Inhand_Salary": {
                0: 2948.0116666666668,
                1: 10046.2575,
                2: 9873.39,
            },
            "Num_Bank_Accounts": {0: 0, 1: 0, 2: 0},
            "Num_Credit_Card": {0: 2, 1: 6, 2: 3},
            "Interest_Rate": {0: 5, 1: 2, 2: 8},
            "Num_of_Loan": {0: "0", 1: "0", 2: "1"},
            "Type_of_Loan": {
                0: "Home Loan",
                1: "Car Loan",
                2: "Personal Loan",
            },
            "Delay_from_due_date": {0: 10, 1: 25, 2: 10},
            "Num_of_Delayed_Payment": {0: "2", 1: "4", 2: "3"},
            "Changed_Credit_Limit": {0: "8.63", 1: "4.53", 2: "5.01"},
            "Num_Credit_Inquiries": {0: 0.0, 1: 4.0, 2: 0.0},
            "Credit_Mix": {0: "Bad", 1: "Bad", 2: "Good"},
            "Outstanding_Debt": {0: "929.04", 1: "14.96", 2: "1388.02"},
            "Credit_Utilization_Ratio": {
                0: 28.99555955433552,
                1: 37.305406548467005,
                2: 28.45691504450972,
            },
            "Credit_History_Age": {
                0: "29 Years and 7 Months",
                1: "22 Years and 3 Months",
                2: "32 Years and 1 Months",
            },
            "Payment_of_Min_Amount": {0: "No", 1: "No", 2: "No"},
            "Total_EMI_per_month": {0: 0.0, 1: 0.0, 2: 59.58605365589474},
            "Amount_invested_monthly": {
                0: "311.2433285195494",
                1: "201.1301814828621",
                2: "626.101931891704",
            },
            "Payment_Behaviour": {
                0: "Low_spent_Small_value_payments",
                1: "High_spent_Large_value_payments",
                2: "Low_spent_Medium_value_payments",
            },
            "Monthly_Balance": {
                0: "273.5578381471173",
                1: "1043.495568517138",
                2: "581.6510144524012",
            },
            "Credit_Score": {0: "Good", 1: "Poor", 2: "Standard"},
        }
    )

    result = Cs2DataSetPreProcessing.process(mock_df)

    expected_result = pd.DataFrame(
        {
            "Age": {0: 24, 1: 29, 2: 48},
            "Occupation": {0: "Entrepreneur", 1: "Writer", 2: "Engineer"},
            "Monthly_Inhand_Salary": {0: 2948.01, 1: 10046.26, 2: 9873.39},
            "Num_Bank_Accounts": {0: 0, 1: 0, 2: 0},
            "Num_Credit_Card": {0: 2, 1: 6, 2: 3},
            "Interest_Rate": {0: 5, 1: 2, 2: 8},
            "Num_of_Loan": {0: 0, 1: 0, 2: 1},
            "Delay_from_due_date": {0: 10, 1: 25, 2: 10},
            "Num_of_Delayed_Payment": {0: 2, 1: 4, 2: 3},
            "Changed_Credit_Limit": {0: 8.63, 1: 4.53, 2: 5.01},
            "Num_Credit_Inquiries": {0: 0, 1: 4, 2: 0},
            "Credit_Mix": {0: "Bad", 1: "Bad", 2: "Good"},
            "Outstanding_Debt": {0: 929.04, 1: 14.96, 2: 1388.02},
            "Credit_Utilization_Ratio": {
                0: 28.99555955433552,
                1: 37.305406548467005,
                2: 28.45691504450972,
            },
            "Credit_History_Age": {0: 355, 1: 267, 2: 385},
            "Payment_of_Min_Amount": {0: "No", 1: "No", 2: "No"},
            "Total_EMI_per_month": {0: 0.0, 1: 0.0, 2: 59.58605365589474},
            "Amount_invested_monthly": {
                0: 311.2433285195494,
                1: 201.1301814828621,
                2: 626.101931891704,
            },
            "Monthly_Balance": {
                0: 273.5578381471173,
                1: 1043.495568517138,
                2: 581.6510144524012,
            },
            "Credit_Score": {0: "Good", 1: "Poor", 2: "Standard"},
            "type_of_loan_Home Loan": {0: 1, 1: 0, 2: 0},
            "type_of_loan_Car Loan": {0: 0, 1: 1, 2: 0},
            "type_of_loan_Personal Loan": {0: 0, 1: 0, 2: 1},
            "Spent_Habit": {
                0: "Low_spent",
                1: "High_spent",
                2: "Low_spent",
            },
            "Payment_Habit": {
                0: "Small_value_payments",
                1: "Large_value_payments",
                2: "Medium_value_payments",
            },
        }
    )

    pd.testing.assert_frame_equal(
        result.sort_index(axis=1), expected_result.sort_index(axis=1)
    )


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


def test_process_negative_num_bank_accounts():
    mock_series = pd.Series([6, -1, 5, -1, 7, -1, 8])

    result = Cs2DataSetPreProcessing.process_negative_num_bank_accounts(mock_series)

    expected_result = pd.Series([6, 0, 5, 0, 7, 0, 8])

    pd.testing.assert_series_equal(result, expected_result)


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


def test_process_outstanding_debt():

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
            "Outstanding_Debt": [
                "2000.12",
                "3000.0",
                "3600.23_",
                "1000.0",
                "2400.0_",
                "2300.0_",
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_outstanding_debt(mock_df)

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
            "Outstanding_Debt": [2000.12, 3000.0, 3600.23, 1000.0, 2400.0, 2300.0],
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


def test_process_payment_of_min_amount():
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
            "Payment_of_Min_Amount": [
                "Yes",
                "NM",
                "Yes",
                "No",
                "NM",
                "NM",
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_payment_of_min_amount(mock_df)

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
            "Payment_of_Min_Amount": [
                "Yes",
                "Yes",
                "Yes",
                "No",
                "No",
                "No",
            ],
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


def test_process_payment_behaviour():
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
            "Payment_Behaviour": [
                "Low_spent_Large_value_payments",
                "Low_spent_Large_value_payments",
                "!@9#%8",
                "Medium_spent_Small_value_payments",
                "!@9#%8",
                "Medium_spent_Small_value_payments",
            ],
        }
    )

    result = Cs2DataSetPreProcessing.process_payment_behaviour(mock_df)

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
            "Spent_Habit": [
                "Low_spent",
                "Low_spent",
                "Low_spent",
                "Medium_spent",
                "Medium_spent",
                "Medium_spent",
            ],
            "Payment_Habit": [
                "Large_value_payments",
                "Large_value_payments",
                "Large_value_payments",
                "Small_value_payments",
                "Small_value_payments",
                "Small_value_payments",
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
