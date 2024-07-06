import pandas as pd
from utils.dataframe_treatment import treat_column_values, treat_columns_names


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


def test_treat_column_values():
    # Test with standard column values
    df = pd.DataFrame(
        {
            "Name": ["John Doe", "Jane Smith", "Alice O'Connor"],
            "Address": ["123 Main St.", "456 Elm St.", "789 Maple Ave."],
            "Age": [30, 40, 50],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Name": ["john_doe", "jane_smith", "alice_oconnor"],
            "Address": ["123_main_st", "456_elm_st", "789_maple_ave"],
            "Age": [30, 40, 50],
        }
    )
    result_df = treat_column_values(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Test with already treated column values
    df = pd.DataFrame(
        {
            "Name": ["john_doe", "jane_smith", "alice_oconnor"],
            "Address": ["123_main_st", "456_elm_st", "789_maple_ave"],
            "Age": [30, 40, 50],
        }
    )
    result_df = treat_column_values(df)
    pd.testing.assert_frame_equal(result_df, df)

    # Test with mixed case and special characters
    df = pd.DataFrame(
        {
            "Name": ["John-Doe", "Jane!Smith", "Alice O'Connor"],
            "Address": ["123 Main St.", "456 Elm St.", "789 Maple Ave."],
            "Age": [30, 40, 50],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Name": ["johndoe", "janesmith", "alice_oconnor"],
            "Address": ["123_main_st", "456_elm_st", "789_maple_ave"],
            "Age": [30, 40, 50],
        }
    )
    result_df = treat_column_values(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Test with special characters
    df = pd.DataFrame(
        {
            "Name": ["John@Doe", "Jane#Smith", "Alice O'Connor"],
            "Address": ["123 Main St.", "456 Elm St.", "789 Maple Ave."],
            "Age": [30, 40, 50],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Name": ["johndoe", "janesmith", "alice_oconnor"],
            "Address": ["123_main_st", "456_elm_st", "789_maple_ave"],
            "Age": [30, 40, 50],
        }
    )
    result_df = treat_column_values(df)
    pd.testing.assert_frame_equal(result_df, expected_df)
