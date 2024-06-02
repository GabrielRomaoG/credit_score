import pandas as pd
from numpy import NaN


class Cs2DataSetPreProcessing:
    @staticmethod
    def process_type_of_loan(cs2_dataset: pd.DataFrame):

        process_df = cs2_dataset.copy()

        process_df["Type_of_Loan"] = (
            process_df["Type_of_Loan"]
            .fillna("")
            .astype(str)
            .str.replace(" and", "")
            .apply(lambda x: x.split(", ") if x else NaN)
        )

        exploded_data = process_df.explode("Type_of_Loan")

        dummies = pd.get_dummies(
            exploded_data["Type_of_Loan"], prefix="type_of_loan", dtype=int
        )

        process_df = (
            exploded_data.join(dummies)
            .groupby(level=0)
            .max()
            .drop(columns=["Type_of_Loan"])
        )

        return process_df
