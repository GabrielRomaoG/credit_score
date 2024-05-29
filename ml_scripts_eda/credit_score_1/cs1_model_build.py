import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import sys


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """Preprocess the data: Split into features and target."""
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
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
        penalty="l1", dual=False, max_iter=10000, solver="liblinear", C=2
    )

    logreg_pipe = Pipeline(
        [("cols_trans", col_trans), ("scaler", scaler), ("linear_svc", logreg)]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    logreg_pipe.fit(X_train, y_train)

    return logreg_pipe


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

    save_model(model, output_model_file)
