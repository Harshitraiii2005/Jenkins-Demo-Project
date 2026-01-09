import pandas as pd

def load_data(data_path: str) -> pd.DataFrame:
    df = pd.read_csv(data_path)

    print(f"Dataset shape: {df.shape}")
    print(f"First 5 rows:\n{df.head()}")
    print(f"Last 5 rows:\n{df.tail()}")
    print(df.info())

    return df
