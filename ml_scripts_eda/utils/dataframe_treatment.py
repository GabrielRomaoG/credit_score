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
