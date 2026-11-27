# 02 – NASA Datasets & Instruments

| Variable | Mission / Instrument | Resolution (approx.) | Use in farming | Access |
|---|---|---|---|---|
| Soil moisture | **SMAP** (L3/L4; 1 km / 9 km downscaled products exist) | 36 km raw, 9 km, 1 km (derived) | Planting timing, irrigation, drought | Earthdata / NSIDC DAAC / Crop-CASMA |
| Precipitation | **GPM IMERG** | ~10 km, 30 min–daily | Rain events, flood/drought risk | GES DISC, Giovanni |
| Vegetation / crop health | **MODIS** (NDVI/EVI), **VIIRS** | 250 m–1 km | Crop condition, phenology | LP DAAC, Worldview, AppEEARS |
| Higher-res vegetation | **HLS** (Landsat + Sentinel-2 harmonized) | 30 m | Field-level monitoring | LP DAAC / CMR-STAC |
| Terrain | **NASADEM** | 30 m | Slope, drainage, erosion | LP DAAC |
| Evapotranspiration / plant stress | **ECOSTRESS** | ~70 m | Water stress | LP DAAC |
| Groundwater | **GRACE-FO** | ~300 km | Irrigation water availability | PO.DAAC / GRACE Tellus |
| Weather & solar (agro-climate) | **NASA POWER** | 0.5° | Temperature, radiation, rainfall time series | POWER API / DAV |

## Notes
- Check each product's **latency** (near-real-time vs. research-grade) before promising "live" features.
- Coarse data (GRACE, SMAP 36 km) is good for *regional* insight; use HLS/MODIS for *field* insight.
- Always record dataset **version + DOI** in your submission's Data & Resources section.
