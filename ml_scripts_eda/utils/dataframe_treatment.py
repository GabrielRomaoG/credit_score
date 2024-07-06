import re
from pandas import DataFrame


def treat_columns_names(df: DataFrame) -> DataFrame:
    """
    Replaces spaces in column names with underscores and converts all characters to lowercase.

    Args:
        df (DataFrame): The DataFrame whose column names need to be treated.

    Returns:
        DataFrame: The DataFrame with treated column names.
    """
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.lower()
    return df


def treat_column_values(df: DataFrame) -> DataFrame:
    """
    Treat the values of non-numeric columns in a DataFrame.
    Removes special characters (except apostrophes), replaces spaces with underscores, and converts to uppercase.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with treated values.
    """

    # Function to process each value
    def process_value(value):
        if isinstance(value, str):
            value = re.sub(r"[^\w\s]", "", value)
            value = value.replace(" ", "_")
            value = value.lower()
        return value

    non_numeric_cols = df.select_dtypes(include=["object"]).columns

    for col in non_numeric_cols:
        df[col] = df[col].apply(process_value)

    return df
