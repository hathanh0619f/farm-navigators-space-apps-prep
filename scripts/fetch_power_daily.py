"""Fetch daily agro-climate data from NASA POWER (no login needed).

Example:
    python scripts/fetch_power_daily.py --lat 10.03 --lon 105.78 --start 20240101 --end 20241231
"""
import argparse
from pathlib import Path

import pandas as pd
import requests

API = "https://power.larc.nasa.gov/api/temporal/daily/point"
PARAMS = ["T2M", "PRECTOTCORR", "ALLSKY_SFC_SW_DWN", "RH2M", "GWETROOT"]


def fetch(lat: float, lon: float, start: str, end: str) -> pd.DataFrame:
    r = requests.get(
        API,
        params={
            "parameters": ",".join(PARAMS),
            "community": "AG",
            "latitude": lat,
            "longitude": lon,
            "start": start,
            "end": end,
            "format": "JSON",
        },
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()["properties"]["parameter"]
    df = pd.DataFrame(data)
    df.index = pd.to_datetime(df.index, format="%Y%m%d")
    df.index.name = "date"
    return df


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", type=float, required=True)
    ap.add_argument("--lon", type=float, required=True)
    ap.add_argument("--start", required=True, help="YYYYMMDD")
    ap.add_argument("--end", required=True, help="YYYYMMDD")
    ap.add_argument("--out", default="data/raw/power_daily.csv")
    a = ap.parse_args()

    df = fetch(a.lat, a.lon, a.start, a.end)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(a.out)
    print(df.describe())
    print(f"Saved to {a.out}")
