import numpy as np
import pandas as pd
import re
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import category_encoders as ce
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split



def extract_ssd(value):
    if pd.isna(value):
        return np.nan
    match = re.search(r'(\d+)\s*GB', value)
    return int(match.group(1)) if match else np.nan

df["SSD_GB"] = df["SSD"].apply(extract_ssd)
df.drop(columns=["SSD"], inplace=True)



from sklearn.impute import SimpleImputer

num_cols = ["Actual Price", "Rating", "Reviews", "SSD_GB"]
cat_cols = ["Brand", "Core"]

num_imputer = SimpleImputer(strategy="median")
cat_imputer = SimpleImputer(strategy="most_frequent")

df[num_cols] = num_imputer.fit_transform(df[num_cols])
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

df['RAM_GB']=SimpleImputer(strategy='most_frequent').fit_transform(df[['RAM_GB']])
df['Screen_Size']=SimpleImputer(strategy='most_frequent').fit_transform(df[['Screen_Size']])


import re

df["RAM_GB"] = df["Name"].str.extract(r'(\d+)\s*GB').astype(float)
df["Screen_Size"] = df["Name"].str.extract(r'(\d{2})').astype(float)
df["Is_Apple"] = df["Brand"].apply(lambda x: 1 if x == "Apple" else 0)


df.drop(columns=['Name','Model'], inplace=True)
df.drop(columns='Saving', inplace=True)


