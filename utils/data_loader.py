"""Data loading utilities for HeatShieldAI."""

import pandas as pd


def load_dataset(path):
    return pd.read_csv(path)


import rasterio
import numpy as np

from utils.config import NDVI_FILE, LST_FILE


def load_ndvi():

    with rasterio.open(NDVI_FILE) as src:

        ndvi = src.read(1)

    return ndvi


def load_lst():

    with rasterio.open(LST_FILE) as src:

        lst = src.read(1)

    return lst


def average_ndvi():

    ndvi = load_ndvi()

    return float(np.nanmean(ndvi))


def max_temperature():

    lst = load_lst()

    return float(np.nanmax(lst))


def average_temperature():

    lst = load_lst()

    return float(np.nanmean(lst))