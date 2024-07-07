from numpy import nan
import pandas as pd
import numpy as np
from utils.dataframe_treatment import treat_column_values, treat_columns_names


class Cs2DataSetPreProcessing:
    """
    Process the DataFrame generated by the `credit_score_dataset_2.csv` file.

    I dropped the columns that the user can't answer easily or can't answer at all for ux purposes.

    Parameters:
        cs2_dataset (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: The processed DataFrame.
    """

    @classmethod
    def process(cls, cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        process_df = cs2_dataset.copy()
        process_df = cls.process_age(process_df)
        process_df["Num_Bank_Accounts"] = cls.process_negative_num_bank_accounts(
            process_df["Num_Bank_Accounts"]
        )
        process_df = cls.process_outliers_from_cols(
            process_df,
            [
                "Num_Bank_Accounts",
                "Num_Credit_Card",
                "Total_EMI_per_month",
            ],
        )
        process_df = cls.process_monthly_inhand_salary(process_df)
        process_df = cls.process_num_of_loan(process_df)
        process_df = cls.process_type_of_loan(process_df)
        process_df = cls.process_num_of_delayed_payment(process_df)
        process_df = cls.process_outstanding_debt(process_df)
        process_df = cls.process_credit_history_age(process_df)
        process_df = cls.process_amount_invested_monthly(process_df)
        process_df = cls.process_payment_behaviour(process_df)
        process_df = cls.process_monthly_balance(process_df)
        process_df = process_df.drop(
            columns=[
                "ID",
                "Customer_ID",
                "Month",
                "Name",
                "SSN",
                "Annual_Income",
                "Occupation",
                "Interest_Rate",
                "Changed_Credit_Limit",
                "Num_Credit_Inquiries",
                "Credit_Mix",
                "Delay_from_due_date",
                "Payment_of_Min_Amount",
            ]
        )
        process_df = treat_columns_names(process_df)
        process_df = treat_column_values(process_df)
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

        def adjust_age_to_mode(grouped_age):
            mode_age = grouped_age.mode()[0]

            condition = (grouped_age < (mode_age - 1)) | (grouped_age > (mode_age + 1))

            grouped_age.loc[condition] = mode_age

            return grouped_age

        cs2_dataset["Age"] = cs2_dataset.groupby("Customer_ID")["Age"].transform(
            adjust_age_to_mode
        )

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
    def process_negative_num_bank_accounts(
        num_bank_accounts_col: pd.Series,
    ) -> pd.Series:
        """
        Process the 'num_bank_accounts_col' series by replacing any negative values with 0.

        Parameters:
            num_bank_accounts_col (pd.Series): The series containing the number of bank accounts.

        Returns:
            pd.Series: The processed series with negative values replaced by 0.
        """
        num_bank_accounts_col = num_bank_accounts_col.replace(-1, 0)

        return num_bank_accounts_col

    @staticmethod
    def process_outliers_from_cols(
        cs2_dataset: pd.DataFrame, cols: list[str]
    ) -> pd.DataFrame:
        """
        Process the specified columns in the given DataFrame.

        Calculate the mode grouped by the customer_id and compare each row with the mode.
        If the value is greater than 2 times the mode, it will be replaced by the mode.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame to process.
            cols (list): The list of column names to process.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        cs2_dataset_grouped_customer = cs2_dataset.groupby("Customer_ID")
        for col in cols:
            mode_by_customer = cs2_dataset_grouped_customer[col].transform(
                lambda x: x.mode()[0]
            )
            threshold = mode_by_customer * 2
            cs2_dataset[col] = np.where(
                cs2_dataset[col] > threshold, mode_by_customer, cs2_dataset[col]
            )

        return cs2_dataset

    @staticmethod
    def process_num_of_loan(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Num_of_Loan' column in the given DataFrame.

        Removes non-numeric characters, sets negative values and missing values with the median grouped by customer,
        update the column type to integer and returns the modified DataFrame.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the 'Num_of_Loan' column.

        Returns:
            pd.DataFrame: The modified DataFrame with the processed 'Num_of_Loan' column.
        """
        cs2_dataset["Num_of_Loan"] = (
            cs2_dataset["Num_of_Loan"]
            .replace(r"[^0-9\-]", "", regex=True)
            .astype(float)
        )

        cs2_dataset["Num_of_Loan"] = cs2_dataset["Num_of_Loan"].where(
            (cs2_dataset["Num_of_Loan"] >= 0),
            nan,
        )

        def adjust_num_of_delayed_payment_to_median(grouped_num_of_loan):
            median = grouped_num_of_loan.median()

            condition = (grouped_num_of_loan > 2 * median) | (
                pd.isna(grouped_num_of_loan)
            )

            grouped_num_of_loan = np.where(condition, median, grouped_num_of_loan)

            return grouped_num_of_loan

        cs2_dataset["Num_of_Loan"] = (
            cs2_dataset.groupby("Customer_ID")["Num_of_Loan"]
            .transform(adjust_num_of_delayed_payment_to_median)
            .astype(int)
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

        Removes non-numeric characters, sets negative values and missing values with the mode grouped by customer,
        update the column type to integer and returns the modified DataFrame.

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
            (cs2_dataset["Num_of_Delayed_Payment"] >= 0),
            nan,
        )

        def adjust_num_of_delayed_payment_to_median(grouped_num_of_delayed_payment):
            median = grouped_num_of_delayed_payment.median()

            condition = (grouped_num_of_delayed_payment > 2 * median) | (
                pd.isna(grouped_num_of_delayed_payment)
            )

            grouped_num_of_delayed_payment = np.where(
                condition, median, grouped_num_of_delayed_payment
            )

            return grouped_num_of_delayed_payment

        cs2_dataset["Num_of_Delayed_Payment"] = (
            cs2_dataset.groupby("Customer_ID")["Num_of_Delayed_Payment"]
            .transform(adjust_num_of_delayed_payment_to_median)
            .astype(int)
        )

        return cs2_dataset

    @staticmethod
    def process_outstanding_debt(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Outstanding_Debt' column in the given DataFrame.

        Keep only the numeric characters in the 'Outstanding_Debt' column and convert it to an integer.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the 'Occupation' column.

        Returns:
            pd.DataFrame: The modified DataFrame with the processed 'Occupation' column.
        """
        cs2_dataset["Outstanding_Debt"] = (
            cs2_dataset["Outstanding_Debt"]
            .str.replace(r"[^0-9\.]", "", regex=True)
            .astype(float)
        )

        return cs2_dataset

    @staticmethod
    def process_credit_history_age(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Credit_History_Age' column of the given DataFrame by parsing the age string into years and months,
        and then calculating the age in months. The nan values are filled with the mean age for each customer. The processed DataFrame is returned.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the 'Credit_History_Age' column.

        Returns:
            pd.DataFrame: The processed DataFrame with the 'Credit_History_Age' column filled with the calculated age in months.
        """

        def parse_age(age_str):
            if pd.isna(age_str):
                return age_str
            years = int(age_str.split(" Years")[0])
            months_part = age_str.split(" and ")[-1]
            months = int(months_part.split(" Months")[0])
            return years * 12 + months

        cs2_dataset["Credit_History_Age"] = cs2_dataset["Credit_History_Age"].apply(
            parse_age
        )

        cs2_dataset["Credit_History_Age"] = (
            cs2_dataset.groupby("Customer_ID")["Credit_History_Age"]
            .transform(lambda x: x.fillna(x.mode()[0]))
            .astype(int)
        )

        return cs2_dataset

    @staticmethod
    def process_amount_invested_monthly(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Amount_invested_monthly' column in the given pandas DataFrame.

        Replaces '__10000__' with nan, converts to float, and fills nan values with the means grouped by Customer_ID.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame to process.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        cs2_dataset["Amount_invested_monthly"] = (
            cs2_dataset["Amount_invested_monthly"]
            .replace("__10000__", nan)
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
    def process_payment_behaviour(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the Payment_Behaviour column in the given DataFrame.

        This function processes the Payment_Behaviour column by splitting it into two new columns: Spent_Habit and Payment_Habit.
        It replaces the "!@9#%8" substring with an empty string in each value of the Payment_Behaviour column.
        It then splits each value of the Payment_Behaviour column by "_" and assigns the first part to Spent_Habit and the second part to Payment_Habit.
        Finally, it replaces an empty string values in the Spent_Habit and Payment_Habit columns with the mode by Customer_ID and drops the original Payment_Behaviour column from the DataFrame.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame containing the Payment_Behaviour column.

        Returns:
            pd.DataFrame: The DataFrame with the processed Payment_Behaviour column.
        """
        cs2_dataset["Payment_Behaviour"] = cs2_dataset["Payment_Behaviour"].replace(
            "!@9#%8", nan
        )

        def split_second_underscore(value):
            if pd.isna(value):
                return pd.Series([nan, nan])
            parts = value.split("_")
            if len(parts) > 2:
                return pd.Series(["_".join(parts[:2]), "_".join(parts[2:])])

        cs2_dataset[["Spent_Habit", "Payment_Habit"]] = cs2_dataset[
            "Payment_Behaviour"
        ].apply(split_second_underscore)

        cs2_dataset[["Spent_Habit", "Payment_Habit"]] = cs2_dataset.groupby(
            "Customer_ID"
        )[["Spent_Habit", "Payment_Habit"]].transform(lambda x: x.fillna(x.mode()[0]))

        cs2_dataset.drop("Payment_Behaviour", axis=1, inplace=True)

        return cs2_dataset

    @staticmethod
    def process_monthly_balance(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process the 'Monthly_Balance' column in the given pandas DataFrame.

        Replaces '__' with nan, converts to float, and fills nan values with the means grouped by Customer_ID.

        Parameters:
            cs2_dataset (pd.DataFrame): The DataFrame to process.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        mask = cs2_dataset["Monthly_Balance"].str.contains("__", na=False)

        cs2_dataset.loc[mask, "Monthly_Balance"] = nan

        cs2_dataset["Monthly_Balance"] = cs2_dataset["Monthly_Balance"].astype(float)

        means = cs2_dataset.groupby("Customer_ID")["Monthly_Balance"].transform("mean")

        cs2_dataset["Monthly_Balance"] = cs2_dataset["Monthly_Balance"].fillna(means)

        return cs2_dataset
