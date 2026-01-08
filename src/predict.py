import pandas as pd
import joblib
import os

def load_artifacts():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_path = os.path.join(base_dir, "models")

    model = joblib.load(os.path.join(models_path, "xgboost_model.joblib"))
    label_encoder = joblib.load(os.path.join(models_path, "label_encoder.joblib"))

    return model, label_encoder

def load_data(path):
    return pd.read_csv(path)

def prepare_data(df):
    return df.drop(columns=["Class", "Category", "Filename"], errors="ignore")

if __name__ == "__main__":
    model, label_encoder = load_artifacts()

    # Exemplo de arquivo para predição
    input_file = "../data/malmem2022.csv"

    df = load_data(input_file)
    X = prepare_data(df)

    predictions = model.predict(X)
    labels = label_encoder.inverse_transform(predictions)

    df["Prediction"] = labels

    print(df[["Prediction"]].head())
