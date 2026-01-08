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


num_cols = ["Actual Price", "Rating", "Reviews", "SSD_GB","RAM_GB"]
ohe_cols = ["Brand", "Core"]

target = "Discounted Price"


num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

ohe_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

target_enc_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("target_enc", ce.TargetEncoder())
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", num_pipeline, num_cols),
        ("ohe", ohe_pipeline, ohe_cols)
    ],
    remainder="drop"
)


from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

cat_features = ["Brand", "Core"]

model = CatBoostRegressor(
    iterations=1000,
    learning_rate=0.05,
    depth=8,
    loss_function="MAE",
    verbose=0
)

pipe = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

pipe.fit(X_train, y_train)
