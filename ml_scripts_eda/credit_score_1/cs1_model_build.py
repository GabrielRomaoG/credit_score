import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (
    GridSearchCV,
    ShuffleSplit,
    cross_validate,
)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import sys
from credit_score_1.cs1_preprocessing import Cs1DataSetPreProcessing


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """Preprocess the data"""

    list_feat_rfe = [
        "gender",
        "education",
        "age",
        "income",
    ]

    data = Cs1DataSetPreProcessing.process(data)

    X = data[list_feat_rfe]
    y = data["credit_score"]
    return X, y


def train_model(X, y):
    """Train a Logistic Regression model with preprocessing pipeline."""
    categorical_cols = X.select_dtypes("object").columns

    col_trans = ColumnTransformer(
        [
            ("ohe", OneHotEncoder(), categorical_cols),
        ],
        remainder="passthrough",
        verbose_feature_names_out=False,
    )

    scaler = StandardScaler()

    logreg = LogisticRegression(
        dual=False, max_iter=10000, penalty="elasticnet", solver="saga"
    )

    logreg_pipe = Pipeline(
        [
            ("cols_trans", col_trans),
            ("scaler", scaler),
            ("logreg", logreg),
        ]
    )

    param_grid = {
        "logreg__C": np.linspace(0.1, 5, 10),
        "logreg__l1_ratio": np.linspace(0, 1, 5),
    }

    grid_search_logreg = GridSearchCV(
        logreg_pipe, param_grid, cv=5, scoring="accuracy", n_jobs=-1, verbose=1
    )

    outer_valid = ShuffleSplit(n_splits=1, test_size=0.20, random_state=2)

    results_logreg = cross_validate(
        estimator=grid_search_logreg, X=X, y=y, cv=outer_valid, return_estimator=True
    )

    print(f"accuracy: {results_logreg['test_score']}")

    return results_logreg


def save_model(model, file_name):
    """Save the trained model to a file."""
    joblib.dump(model, file_name)
    print(f"Model saved to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python train_model.py <csv_file_path> <output_model_file>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    output_model_file = sys.argv[2]

    data = load_data(csv_file_path)
    X, y = preprocess_data(data)

    model = train_model(X, y)

    save_model(model, output_model_file + ".z")
