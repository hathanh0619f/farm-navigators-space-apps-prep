# 03 – Data Access Guide

## Accounts
- NASA Earthdata Login (free): https://urs.earthdata.nasa.gov/

## Portals & tools
| Tool | Purpose | Link |
|---|---|---|
| Worldview | Visual exploration of layers | https://worldview.earthdata.nasa.gov/ |
| Earthdata Search | Find & download granules | https://search.earthdata.nasa.gov/ |
| AppEEARS | Point/area sample extraction (MODIS, etc.) | https://appeears.earthdatacloud.nasa.gov/ |
| Giovanni | Quick time-series & maps (GES DISC) | https://giovanni.gsfc.nasa.gov/giovanni/ |
| NASA POWER DAV / API | Agro-climate time series | https://power.larc.nasa.gov/ |
| NSIDC (SMAP) | Soil moisture data | https://nsidc.org/data/smap |
| Crop-CASMA (USDA/NASA/GMU) | 1 km soil moisture & vegetation for the U.S. | search "Crop-CASMA" |

## Python libraries
`earthaccess`, `xarray`, `rioxarray`, `rasterio`, `pystac-client`, `geopandas`, `requests`, `pandas`.

## Example: earthaccess
```python
import earthaccess
earthaccess.login()  # uses Earthdata credentials
results = earthaccess.search_data(
    short_name="SPL3SMP_E",  # SMAP L3 enhanced (verify the current short name/version)
    bounding_box=(105.0, 9.5, 106.5, 11.0),
    temporal=("2024-06-01", "2024-06-30"),
)
files = earthaccess.download(results, "data/raw/smap")
```

## Example: NASA POWER (no login)
See `scripts/fetch_power_daily.py`.

## Tips
- Verify product short names/versions in Earthdata Search before coding.
- Cache everything under `data/raw` (git-ignored).
- Prepare a *fallback sample dataset* so the demo works offline.
