import pandas as pd
import numpy as np
import re
from sklearn.impute import SimpleImputer

def extract_ssd(value):
    if pd.isna(value):
        return np.nan
    match = re.search(r'(\d+)\s*GB', str(value))
    return int(match.group(1)) if match else np.nan


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    
    df["SSD_GB"] = df["SSD"].apply(extract_ssd)
    df.drop(columns=["SSD"], inplace=True)


    df["RAM_GB"] = df["Name"].str.extract(r'(\d+)\s*GB').astype(float)
    df["Screen_Size"] = df["Name"].str.extract(r'(\d{2})').astype(float)

    
    df["Is_Apple"] = df["Brand"].apply(lambda x: 1 if x == "Apple" else 0)

    
    df.drop(columns=["Name", "Model", "Saving"], inplace=True)

   
    num_cols = ["Actual Price", "Rating", "Reviews", "SSD_GB", "RAM_GB", "Screen_Size"]
    cat_cols = ["Brand", "Core"]

    df[num_cols] = SimpleImputer(strategy="median").fit_transform(df[num_cols])
    df[cat_cols] = SimpleImputer(strategy="most_frequent").fit_transform(df[cat_cols])
    

    return df
