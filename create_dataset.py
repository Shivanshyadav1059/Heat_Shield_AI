

import pandas as pd
import numpy as np

from utils.data_loader import load_ndvi, load_lst
from utils.config import DATASET_FILE

# -------------------------
# Load raster data
# -------------------------

ndvi = load_ndvi()
lst = load_lst()

# -------------------------
# Flatten arrays
# -------------------------

ndvi = ndvi.flatten()
lst = lst.flatten()

# -------------------------
# Keep only valid pixels
# -------------------------

mask = (
    np.isfinite(ndvi) &
    np.isfinite(lst)
)

ndvi = ndvi[mask]
lst = lst[mask]

# -------------------------
# Keep valid NDVI and LST values
# -------------------------

mask = (
    (ndvi >= -1) &
    (ndvi <= 1) &
    (lst > 0)
)

ndvi = ndvi[mask]
lst = lst[mask]

# -------------------------
# Normalize values
# -------------------------

lst_norm = (lst - lst.min()) / (lst.max() - lst.min())
ndvi_norm = (ndvi + 1) / 2

# -------------------------
# Create Heat Risk
# -------------------------

risk = (
    lst_norm * 70 +
    (1 - ndvi_norm) * 30
)

# -------------------------
# Create DataFrame
# -------------------------

df = pd.DataFrame({
    "NDVI": ndvi,
    "LST": lst,
    "Risk": risk
})

# -------------------------
# Save Dataset
# -------------------------

df.to_csv(DATASET_FILE, index=False)

print("\n✅ Dataset Created Successfully!\n")
print(df.head())
print("\nTotal Samples:", len(df))
print("\nStatistics:\n")
print(df.describe())