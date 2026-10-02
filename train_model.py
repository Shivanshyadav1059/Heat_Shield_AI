# """Train a heat prediction model."""

# import joblib
# from sklearn.ensemble import RandomForestRegressor


# def train_model(dataset_path="data/dataset.csv", model_path="models/heat_model.pkl"):
#     # Placeholder train function. Replace with actual model training logic.
#     print(f"Training model using dataset: {dataset_path}")
#     model = RandomForestRegressor(n_estimators=10)
#     joblib.dump(model, model_path)
#     print(f"Model saved to {model_path}")


# if __name__ == "__main__":
#     train_model()

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from utils.config import DATASET_FILE, MODEL_FILE

print("Loading dataset...")

df = pd.read_csv(DATASET_FILE)

print(f"Dataset Loaded: {len(df):,} samples")

# -------------------------
# Features and Target
# -------------------------

X = df[["NDVI", "LST"]]
y = df["Risk"]

# -------------------------
# Train/Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print(f"Training Samples : {len(X_train):,}")
print(f"Testing Samples  : {len(X_test):,}")

# -------------------------
# Train Model
# -------------------------

print("\nTraining Random Forest...")

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# -------------------------
# Predictions
# -------------------------

pred = model.predict(X_test)

# -------------------------
# Evaluation
# -------------------------

mae = mean_absolute_error(y_test, pred)
rmse = mean_squared_error(y_test, pred) ** 0.5
r2 = r2_score(y_test, pred)

print("\n========== MODEL PERFORMANCE ==========")
print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")

# -------------------------
# Feature Importance
# -------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========")
print(importance)

# -------------------------
# Save Model
# -------------------------

joblib.dump(model, MODEL_FILE)

print("\n✅ Model Saved Successfully!")
print(f"Location: {MODEL_FILE}")