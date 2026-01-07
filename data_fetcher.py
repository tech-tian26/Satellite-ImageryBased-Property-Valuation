"""
data_fetcher.py

Downloads satellite images for real estate properties using
latitude and longitude coordinates via Mapbox Static Images API.

This script is intended for one-time data acquisition.
"""

import os
import time
import requests
import pandas as pd
from PIL import Image
from io import BytesIO

# ========================
# CONFIGURATION
# ========================

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")  # MUST be set externally
STYLE = "mapbox/satellite-v9"
ZOOM = 16
IMG_SIZE = "224x224"
DELAY = 0.2  # seconds between requests (rate limiting)

# ========================
# IMAGE FETCH FUNCTION
# ========================

def fetch_mapbox_image(lat, lon, save_path):
    """
    Fetch a satellite image for given latitude & longitude
    and save it to disk.
    """
    if os.path.exists(save_path):
        return True

    url = (
        f"https://api.mapbox.com/styles/v1/{STYLE}/static/"
        f"{lon},{lat},{ZOOM}/{IMG_SIZE}"
        f"?access_token={MAPBOX_TOKEN}"
    )

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.save(save_path)
            return True
        else:
            print(f"Failed [{response.status_code}] for {lat}, {lon}")
            return False
    except Exception as e:
        print("Error:", e)
        return False

# ========================
# DATASET IMAGE DOWNLOAD
# ========================

def download_dataset_images(
    csv_path,
    id_column,
    lat_column,
    lon_column,
    output_dir
):
    """
    Download images for all rows in a CSV file.
    """
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_path)

    for idx, row in df.iterrows():
        property_id = row[id_column]
        img_path = os.path.join(output_dir, f"{property_id}.png")

        fetch_mapbox_image(
            lat=row[lat_column],
            lon=row[lon_column],
            save_path=img_path
        )

        time.sleep(DELAY)

# ========================
# MAIN (OPTIONAL EXECUTION)
# ========================

if __name__ == "__main__":
    """
    Example usage (paths are examples):

    export MAPBOX_TOKEN=your_token_here

    python data_fetcher.py
    """

    download_dataset_images(
        csv_path="data/train.csv",
        id_column="id",
        lat_column="lat",
        lon_column="long",
        output_dir="images/train"
    )

    download_dataset_images(
        csv_path="data/test.csv",
        id_column="id",
        lat_column="lat",
        lon_column="long",
        output_dir="images/test"
    )
