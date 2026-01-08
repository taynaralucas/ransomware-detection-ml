import pandas as pd
from sklearn.model_selection import train_test_split

DATASET_PATH = "../data/malmem2022.csv"

def load_dataset(path):
    return pd.read_csv(path)

def prepare_data(df):
    # Variável alvo
    y = df["Class"]

    # Removendo colunas não utilizadas no modelo
    X = df.drop(columns=["Class", "Category", "Filename"])

    return X, y

if __name__ == "__main__":
    df = load_dataset(DATASET_PATH)
    X, y = prepare_data(df)

    print("Formato de X:", X.shape)
    print("Formato de y:", y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("\nConjunto de treino:", X_train.shape)
    print("Conjunto de teste:", X_test.shape)
