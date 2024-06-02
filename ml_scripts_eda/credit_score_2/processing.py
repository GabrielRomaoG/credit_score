import pandas as pd


class Cs2DataSetPreProcessing:
    @staticmethod
    def process_type_of_loan(cs2_dataset: pd.DataFrame):

        process_df = cs2_dataset.copy()

        process_df["Type_of_Loan"] = (
            process_df["Type_of_Loan"]
            .fillna("")
            .astype(str)
            .str.replace(" and", "")
            .apply(lambda x: x.split(", ") if x else [])
        )

        loan_types = set(
            [loan for sublist in process_df["Type_of_Loan"] for loan in sublist if loan]
        )

        for loan_type in loan_types:
            column_name = f"type_of_loan_{loan_type}"
            process_df[column_name] = process_df["Type_of_Loan"].apply(
                lambda x: 1 if loan_type in x else 0
            )

        process_df.drop(columns=["Type_of_Loan"], inplace=True)

        return process_df
