# 06 – Tech Stack (candidate)

| Layer | Option A | Option B |
|---|---|---|
| Data processing | Python (xarray, rasterio) | Google Earth Engine (if allowed) |
| Backend | FastAPI | Supabase / serverless |
| Frontend | Next.js / React + MapLibre | Streamlit (fastest MVP) |
| Maps | MapLibre GL / Leaflet | Folium |
| AI layer | LLM chat for farmer-friendly explanation | Rule-based advisory |
| Deploy | Vercel + Render | Hugging Face Spaces |

## Architecture sketch
```
NASA APIs/DAACs → ingestion scripts → processed GeoTIFF/Parquet → API → web/mobile UI → farmer advice
```

## Principles
- Ship a working demo with real NASA data early; polish later.
- Keep an offline sample dataset for the live presentation.
- Document data sources in the repo README for the submission.
