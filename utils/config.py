"""Configuration settings for HeatShieldAI."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data")
MODELS_PATH = os.path.join(BASE_DIR, "models")
IMAGES_PATH = os.path.join(BASE_DIR, "images")


from pathlib import Path

# -------------------------
# Project Root
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Folders
# -------------------------

DATA_DIR = BASE_DIR / "data"
IMAGE_DIR = BASE_DIR / "images"
MODEL_DIR = BASE_DIR / "models"
ASSET_DIR = BASE_DIR / "assets"

# -------------------------
# Files
# -------------------------

NDVI_FILE = DATA_DIR / "lucknow_ndvi_raw.tif"

LST_FILE = DATA_DIR / "lucknow_lst_raw.tif"

DATASET_FILE = DATA_DIR / "dataset.csv"

MODEL_FILE = MODEL_DIR / "heat_model.pkl"

HEAT_MAP = IMAGE_DIR / "heat_map.png"

HOTSPOT_MAP = IMAGE_DIR / "hotspot_map.png"

NDVI_MAP = IMAGE_DIR / "ndvi_map.png"