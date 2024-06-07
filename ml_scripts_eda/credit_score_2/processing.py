from numpy import NaN
import pandas as pd


class Cs2DataSetPreProcessing:
    @classmethod
    def process(cls, cs2_dataset: pd.DataFrame) -> pd.DataFrame:
        process_df = cs2_dataset.copy()
        process_df = cls.process_monthly_inhand_salary(process_df)
        process_df = cls.process_type_of_loan(process_df)
        process_df = cls.process_num_of_delayed_payment(process_df)
        process_df = cls.process_credit_history_age(process_df)
        process_df = cls.process_amount_invested_monthly(process_df)
        process_df = cls.process_monthly_balance(process_df)

        return process_df

    @staticmethod
    def process_monthly_inhand_salary(cs2_dataset: pd.DataFrame) -> pd.DataFrame:

        means = cs2_dataset.groupby("Customer_ID")["Monthly_Inhand_Salary"].transform(
            "mean"
        )

        cs2_dataset["Monthly_Inhand_Salary"] = cs2_dataset[
            "Monthly_Inhand_Salary"
        ].fillna(means)

        return cs2_dataset

    @staticmethod
    def process_type_of_loan(cs2_dataset: pd.DataFrame) -> pd.DataFrame:

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

        mask = cs2_dataset["Monthly_Balance"].str.contains("__", na=False)

        cs2_dataset.loc[mask, "Monthly_Balance"] = NaN

        cs2_dataset["Monthly_Balance"] = cs2_dataset["Monthly_Balance"].astype(float)

        means = cs2_dataset.groupby("Customer_ID")["Monthly_Balance"].transform("mean")

        cs2_dataset["Monthly_Balance"] = cs2_dataset["Monthly_Balance"].fillna(means)

        return cs2_dataset
