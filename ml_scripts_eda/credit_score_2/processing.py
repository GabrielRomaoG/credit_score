from numpy import NaN
import pandas as pd
import numpy as np


class Cs2DataSetPreProcessing:
    """
    Process the DataFrame generated by the `credit_score_dataset_2.csv` file.

    Parameters:
        cs2_dataset (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: The processed DataFrame.
    """

    @classmethod
    def process(cls, cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        process_df = cs2_dataset.copy()
        process_df = cls.process_age(process_df)
        process_df = cls.process_monthly_inhand_salary(process_df)
        process_df = cls.process_type_of_loan(process_df)
        process_df = cls.process_num_of_delayed_payment(process_df)
        process_df = cls.process_credit_history_age(process_df)
        process_df = cls.process_amount_invested_monthly(process_df)
        process_df = cls.process_monthly_balance(process_df)

        return process_df

    @staticmethod
    def process_age(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the age column in the given DataFrame by removing non-numeric characters and converting it to an integer.
        Adjust the age values for each customer to the mode of the age values for that customer.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the age column.

        Returns:
            pd.DataFrame: The DataFrame with the processed age column.
        """
        cs2_dataset["Age"] = (
            cs2_dataset["Age"].str.replace("[^0-9]", "", regex=True).astype(int)
        )

        def adjust_age_to_mode(group):
            mode_age = group["Age"].mode()[0]

            condition = (group["Age"] < (mode_age - 1)) | (
                group["Age"] > (mode_age + 1)
            )

            group.loc[condition, "Age"] = mode_age

            return group

        cs2_dataset = (
            cs2_dataset.groupby("Customer_ID")
            .apply(adjust_age_to_mode)
            .reset_index(drop=True)
        )

        return cs2_dataset

    def process_occupation(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the occupation column in the given DataFrame.

        Replace any row that has "_" in the string with the most common occupation by customer.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the occupation column.

        Returns:
            pd.DataFrame: The DataFrame with the processed occupation column.
        """
        cs2_dataset["Occupation"] = cs2_dataset.groupby("Customer_ID")[
            "Occupation"
        ].transform(lambda x: np.where(x.str.contains("_"), x.mode()[0], x))

        return cs2_dataset

    @staticmethod
    def process_monthly_inhand_salary(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the monthly in-hand salary in the given DataFrame.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the monthly in-hand salary.

        Returns:
            pd.DataFrame: The DataFrame with the processed monthly in-hand salary.
        """
        means = cs2_dataset.groupby("Customer_ID")["Monthly_Inhand_Salary"].transform(
            "mean"
        )

        cs2_dataset["Monthly_Inhand_Salary"] = (
            cs2_dataset["Monthly_Inhand_Salary"].fillna(means).round(2)
        )

        return cs2_dataset

    @staticmethod
    def process_type_of_loan(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the Type_of_Loan column in the given DataFrame.

        This function takes a DataFrame `cs2_dataset` as input and processes the Type_of_Loan column. It performs the following steps:
        1. Fills any missing values in the Type_of_Loan column with an empty string.
        2. Converts the Type_of_Loan column to string type.
        3. Replaces the " and" substring with an empty string in each value of the Type_of_Loan column.
        4. Splits each value of the Type_of_Loan column by ", " and creates a list of loan types.
        5. Creates a set of unique loan types from the list of loan types.
        6. Iterates over each loan type and creates a new column with the name "type_of_loan_{loan_type}". The value of this column is 1 if the loan type is present in the Type_of_Loan column for that row, otherwise it is 0.
        7. Drops the original Type_of_Loan column from the DataFrame.
        8. Returns the modified DataFrame.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the Type_of_Loan column.

        Returns:
            pd.DataFrame: The DataFrame with the processed Type_of_Loan column.
        """
        cs2_dataset["Type_of_Loan"] = (
            cs2_dataset["Type_of_Loan"]
            .fillna("")
            .astype(str)
            .str.replace(" and", "")
            .apply(lambda x: x.split(", ") if x else [])
        )

        loan_types = set(
            [
                loan
                for sublist in cs2_dataset["Type_of_Loan"]
                for loan in sublist
                if loan
            ]
        )

        for loan_type in loan_types:
            column_name = f"type_of_loan_{loan_type}"
            cs2_dataset[column_name] = cs2_dataset["Type_of_Loan"].apply(
                lambda x: 1 if loan_type in x else 0
            )

        cs2_dataset.drop(columns=["Type_of_Loan"], inplace=True)

        return cs2_dataset

    @staticmethod
    def process_num_of_delayed_payment(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Num_of_Delayed_Payment' column in the given DataFrame.

        Removes non-numeric characters, converts to float, sets negative values to 0, fills missing values with mean, and returns the modified DataFrame.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the 'Num_of_Delayed_Payment' column.

        Returns:
            pd.DataFrame: The modified DataFrame with the processed 'Num_of_Delayed_Payment' column.
        """
        cs2_dataset["Num_of_Delayed_Payment"] = (
            cs2_dataset["Num_of_Delayed_Payment"]
            .replace(r"[^0-9\-]", "", regex=True)
            .astype(float)
        )

        cs2_dataset["Num_of_Delayed_Payment"] = cs2_dataset[
            "Num_of_Delayed_Payment"
        ].where(
            (cs2_dataset["Num_of_Delayed_Payment"] >= 0)
            | (pd.isna(cs2_dataset["Num_of_Delayed_Payment"])),
            0,
        )

        means = cs2_dataset.groupby("Customer_ID")["Num_of_Delayed_Payment"].transform(
            "mean"
        )

        cs2_dataset["Num_of_Delayed_Payment"] = cs2_dataset[
            "Num_of_Delayed_Payment"
        ].fillna(means)

        return cs2_dataset

    @staticmethod
    def process_credit_history_age(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Credit_History_Age' column of the given DataFrame by parsing the age string into years and months,
        and then calculating the age in months. The NaN values are filled with the mean age for each customer. The processed DataFrame is returned.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the 'Credit_History_Age' column.

        Returns:
            pd.DataFrame: The processed DataFrame with the 'Credit_History_Age' column filled with the calculated age in months.
        """

        def parse_age(age_str):
            if pd.isna(age_str):
                return age_str
            years, months = 0, 0
            if "years" in age_str:
                years = int(age_str.split(" years")[0])
            if "months" in age_str:
                months_part = age_str.split(" and ")[-1]
                months = int(months_part.split(" months")[0])
            return years * 12 + months

        cs2_dataset["Credit_History_Age"] = (
            cs2_dataset["Credit_History_Age"].apply(parse_age).astype(float)
        )

        means = cs2_dataset.groupby("Customer_ID")["Credit_History_Age"].transform(
            "mean"
        )

        cs2_dataset["Credit_History_Age"] = cs2_dataset["Credit_History_Age"].fillna(
            means
        )

        return cs2_dataset

    @staticmethod
    def process_amount_invested_monthly(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Amount_invested_monthly' column in the given pandas DataFrame.

        Replaces '__10000__' with NaN, converts to float, and fills NaN values with the means grouped by Customer_ID.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame to process.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        cs2_dataset["Amount_invested_monthly"] = (
            cs2_dataset["Amount_invested_monthly"]
            .replace("__10000__", NaN)
            .astype(float)
        )
        means = cs2_dataset.groupby("Customer_ID")["Amount_invested_monthly"].transform(
            "mean"
        )

        cs2_dataset["Amount_invested_monthly"] = cs2_dataset[
            "Amount_invested_monthly"
        ].fillna(means)

        return cs2_dataset

    @staticmethod
    def process_monthly_balance(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Monthly_Balance' column in the given pandas DataFrame.

        Replaces '__' with NaN, converts to float, and fills NaN values with the means grouped by Customer_ID.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame to process.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        mask = cs2_dataset["Monthly_Balance"].str.contains("__", na=False)

        cs2_dataset.loc[mask, "Monthly_Balance"] = NaN

        cs2_dataset["Monthly_Balance"] = cs2_dataset["Monthly_Balance"].astype(float)

        means = cs2_dataset.groupby("Customer_ID")["Monthly_Balance"].transform("mean")

        cs2_dataset["Monthly_Balance"] = cs2_dataset["Monthly_Balance"].fillna(means)

        return cs2_dataset
