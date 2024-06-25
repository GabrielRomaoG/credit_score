import sys
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
from processing import Cs2DataSetPreProcessing


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """Preprocess the data: Split into features and target."""
    list_feat_rfe = [
        "Num_Bank_Accounts",
        "Num_Credit_Card",
        "Num_of_Loan",
        "Num_of_Delayed_Payment",
        "Outstanding_Debt",
        "Credit_History_Age",
        "Total_EMI_per_month",
    ]

    data = Cs2DataSetPreProcessing.process(data)

    y = data["Credit_Score"]
    X = data[list_feat_rfe]

    return X, y


def train_main_model(X, y):
    """Train a HistGradientBoostingClassifier model with preprocessing pipeline."""
    hgbc = HistGradientBoostingClassifier(
        learning_rate=0.1, max_iter=200, max_leaf_nodes=210, min_samples_leaf=7
    ).fit(X, y)

    return hgbc


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

    models_dict = {"main_model": main_model, "logreg_model": logreg_model}

    save_model(models_dict, output_model_file)
