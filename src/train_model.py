import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier

#salvar modelo e label encoder
def save_artifacts(model, label_encoder):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_path = os.path.join(base_dir, "models")

    os.makedirs(models_path, exist_ok=True)

    joblib.dump(model, os.path.join(models_path, "xgboost_model.joblib"))
    joblib.dump(label_encoder, os.path.join(models_path, "label_encoder.joblib"))


DATASET_PATH = "../data/malmem2022.csv"

def load_dataset(path):
    return pd.read_csv(path)

def prepare_data(df):
    # Codificando a variável alvo
    le = LabelEncoder()
    y = le.fit_transform(df["Class"])

    # Features
    X = df.drop(columns=["Class", "Category", "Filename"])

    return X, y, le


def train_xgboost(X_train, y_train):
    model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss",
        
    )
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    df = load_dataset(DATASET_PATH)
    X, y, label_encoder = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = train_xgboost(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\nAcurácia:", accuracy_score(y_test, y_pred))
    print("\nRelatório de classificação:\n")
    print(classification_report(y_test, y_pred))
        
    save_artifacts(model, label_encoder)
    print("\nModelo e LabelEncoder salvos com sucesso.")


