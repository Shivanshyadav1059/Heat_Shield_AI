# """Prediction utilities for HeatShieldAI."""

# import pandas as pd


# def predict_heat_risk(dataset):
#     if "heat_risk" in dataset.columns:
#         return dataset["heat_risk"]
#     return pd.Series([0] * len(dataset), index=dataset.index)



import joblib
import numpy as np

from utils.config import MODEL_FILE

# Load once
model = joblib.load(MODEL_FILE)

def predict_risk(avg_ndvi, max_temp):
    sample = np.array([[avg_ndvi, max_temp]])
    prediction = model.predict(sample)[0]
    return round(float(prediction), 2)