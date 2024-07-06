import pandas as pd
from utils.dataframe_treatment import treat_columns_names


def test_treat_columns_names():
    df = pd.DataFrame({"First Name": [1, 2], "Last Name": [3, 4], "Age": [5, 6]})
    expected_df = pd.DataFrame(
        {"first_name": [1, 2], "last_name": [3, 4], "age": [5, 6]}
    )
    result_df = treat_columns_names(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

    df = pd.DataFrame({"first_name": [1, 2], "last_name": [3, 4], "age": [5, 6]})
    result_df = treat_columns_names(df)
    pd.testing.assert_frame_equal(result_df, df)
