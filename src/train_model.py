import pandas as pd

# Caminho do dataset
DATASET_PATH = "../data/malmem2022.csv"

def load_dataset(path):
    """
    Carrega o dataset a partir de um arquivo CSV.
    """
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_dataset(DATASET_PATH)

    print("Dataset carregado com sucesso!")
    print("Formato do dataset:", df.shape)
    print("\nPrimeiras linhas:")
    print(df.head())