import pandas as pd

DATASET_PATH = "../data/malmem2022.csv"

def load_dataset(path):
    df = pd.read_csv(path)
    return df

def analyze_dataset(df):
    print("Informações gerais do dataset:\n")
    print(df.info())

    print("\nDistribuição das classes:\n")
    print(df["Class"].value_counts())

    print("\nPercentual das classes:\n")
    print(df["Class"].value_counts(normalize=True) * 100)

if __name__ == "__main__":
    df = load_dataset(DATASET_PATH)
    analyze_dataset(df)