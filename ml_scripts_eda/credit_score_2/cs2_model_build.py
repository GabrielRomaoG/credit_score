import sys
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV, ShuffleSplit, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
from credit_score_2.cs2_preprocessing import Cs2DataSetPreProcessing


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """Preprocess the data: Split into features and target."""
    list_feat_rfe = [
        "num_bank_accounts",
        "num_credit_card",
        "num_of_loan",
        "num_of_delayed_payment",
        "outstanding_debt",
        "credit_history_age",
        "total_emi_per_month",
    ]

    data = Cs2DataSetPreProcessing.process(data)

    y = data["credit_score"]
    X = data[list_feat_rfe]

    return X, y


def train_main_model(X, y):
    """Train a HistGradientBoostingClassifier model with preprocessing pipeline."""
    hgbc = HistGradientBoostingClassifier()

    param_grid = {
        "clf__learning_rate": [0.1],
        "clf__max_iter": [150],
        "clf__max_leaf_nodes": [
            210,
        ],
        "clf__min_samples_leaf": [5],
    }
    hgbc_pipe = Pipeline(
        [
            ("clf", hgbc),
        ]
    )

    grid_search_hgbc = GridSearchCV(
        hgbc_pipe, param_grid, cv=5, scoring="accuracy", n_jobs=-1, verbose=2
    )

    outer_valid = ShuffleSplit(n_splits=1, test_size=0.25, random_state=2)

    results = cross_validate(
        estimator=grid_search_hgbc,
        X=X,
        y=y,
        cv=outer_valid,
        return_estimator=True,
    )

    return results


def train_logreg_model(X, y):
    """Train a Logistic Regression model with preprocessing pipeline."""
    logreg = SGDClassifier(loss="log_loss", max_iter=10000)

    logreg_pipe = Pipeline([("scaler", StandardScaler()), ("logreg", logreg)])

    logreg_pipe.fit(X, y)

    return logreg


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

    main_model = train_main_model(X, y)
    logreg_model = train_logreg_model(X, y)

    main_model["logreg_model"] = logreg_model

    save_model(main_model, output_model_file + ".z")
