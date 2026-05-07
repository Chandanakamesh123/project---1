import pandas as pd

def load_dataset(path):

    # Load CSV Dataset
    df = pd.read_csv(path)

    return df

def display_dataset_info(df):

    print("Dataset Shape:", df.shape)

    print("\nDataset Columns:")
    print(df.columns)

    print("\nFirst Five Rows:")
    print(df.head())
