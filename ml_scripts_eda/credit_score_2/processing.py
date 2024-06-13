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
        process_df = cls.process_occupation(process_df)
        process_df = cls.process_outliers_from_cols(
            process_df,
            [
                "Num_Bank_Accounts",
                "Num_Credit_Card",
                "Interest_Rate",
                "Total_EMI_per_month",
            ],
        )
        process_df = cls.process_monthly_inhand_salary(process_df)
        process_df = cls.process_num_of_loan(process_df)
        process_df = cls.process_type_of_loan(process_df)
        process_df = cls.process_num_of_delayed_payment(process_df)
        process_df = cls.process_changed_credit_limit(process_df)
        process_df = cls.process_num_credit_inquiries(process_df)
        process_df = cls.process_credit_mix(process_df)
        process_df = cls.process_outstanding_debt(process_df)
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

        def adjust_age_to_mode(grouped_age):
            mode_age = grouped_age.mode()[0]

            condition = (grouped_age < (mode_age - 1)) | (grouped_age > (mode_age + 1))

            grouped_age.loc[condition] = mode_age

            return grouped_age

        cs2_dataset["Age"] = cs2_dataset.groupby("Customer_ID")["Age"].transform(
            adjust_age_to_mode
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
            NaN,
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
            NaN,
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
    def process_changed_credit_limit(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process 'Changed_Credit_Limit' column in DataFrame.
        Replace non-numeric chars with NaN, convert to float, round to 2 decimal places.
        Fill missing values in each group with mode of the group.

        Parameters:
        - cs2_dataset (pd.DataFrame): The input DataFrame containing the 'Changed_Credit_Limit' column.

        Returns:
        - cs2_dataset (pd.DataFrame): The DataFrame with the 'Changed_Credit_Limit' column processed.
        """
        cs2_dataset["Changed_Credit_Limit"] = (
            cs2_dataset["Changed_Credit_Limit"]
            .replace(r"[^0-9\-\.]", NaN, regex=True)
            .astype(float)
            .round(2)
        )

        cs2_dataset["Changed_Credit_Limit"] = cs2_dataset.groupby("Customer_ID")[
            "Changed_Credit_Limit"
        ].transform(lambda x: x.fillna(x.mode()[0]))

        return cs2_dataset

    @staticmethod
    def process_num_credit_inquiries(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        def adjust_num_credit_inquiries(grouped_num_credit_inquiries):
            median = grouped_num_credit_inquiries.median()

            condition = (grouped_num_credit_inquiries > 2 * median) | (
                pd.isna(grouped_num_credit_inquiries)
            )

            grouped_num_credit_inquiries = np.where(
                condition, median, grouped_num_credit_inquiries
            )

            return grouped_num_credit_inquiries

        cs2_dataset["Num_Credit_Inquiries"] = (
            cs2_dataset.groupby("Customer_ID")["Num_Credit_Inquiries"]
            .transform(adjust_num_credit_inquiries)
            .astype(int)
        )

        return cs2_dataset

    @staticmethod
    def process_credit_mix(cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Process 'Credit_Mix' column in DataFrame.
        Replace "_" with the mode of the group.

        Parameters:
        - cs2_dataset (pd.DataFrame): The input DataFrame containing the 'Credit_Mix' column.

        Returns:
        - cs2_dataset (pd.DataFrame): The DataFrame with the 'Credit_Mix' column processed.
        """
        cs2_dataset["Credit_Mix"] = cs2_dataset["Credit_Mix"].replace("_", NaN)

        cs2_dataset["Credit_Mix"] = cs2_dataset.groupby("Customer_ID")[
            "Credit_Mix"
        ].transform(lambda x: x.fillna(x.mode()[0]))

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
        and then calculating the age in months. The NaN values are filled with the mean age for each customer. The processed DataFrame is returned.

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
