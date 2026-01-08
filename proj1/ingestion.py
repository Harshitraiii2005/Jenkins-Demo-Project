import pandas as pd
import numpy as np

def load_dataset(df -> data_path):
    df = pd.read_csv('data_path')
    print(f"dataset shape is {df.shape}")
    print(f"first five rows: \n{df.head(5)}")
    print(f"last five rows: \n{df.tail(5)}")
    print(f"dataset info: {df.info()}")
    return df

def ingest_runner():
    data_path = 'priceoye_laptops_version_2.csv'
    load_dataset(data_path)