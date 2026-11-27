# 🌾 NASA Space Apps – Farm Navigators: Preparation

Preparation repo for the NASA Space Apps Challenge challenge
**"NASA Farm Navigators: Using NASA Data Exploration in Agriculture"**
([challenge page](https://www.spaceappschallenge.org/2025/challenges/nasa-farm-navigators-using-nasa-data-exploration-in-agriculture/)).

> Goal: understand the problem, know the data, and have tooling ready *before* the hackathon starts, so the 48 hours go into building, not setting up.

## 📁 Repository structure

```
├── docs/
│   ├── 01-challenge-overview.md   # Problem, audience, what judges want
│   ├── 02-nasa-datasets.md        # SMAP, GPM, MODIS, HLS, POWER, GRACE-FO ...
│   ├── 03-data-access-guide.md    # Earthdata login, APIs, tools, code snippets
│   ├── 04-existing-solutions.md   # Crop-CASMA, NASA Harvest, etc. (benchmark)
│   ├── 05-ideas.md                # Idea backlog + scoring
│   ├── 06-tech-stack.md           # Candidate stack and architecture
│   ├── 07-team-roles.md           # Roles, responsibilities
│   └── 08-hackathon-timeline.md   # 48h plan + submission checklist
├── notebooks/                     # Exploration notebooks
├── src/                           # Reusable code (data fetchers, helpers)
├── scripts/                       # CLI scripts
├── data/raw | data/processed      # Local data (git-ignored)
└── assets/                        # Images, diagrams, pitch material
```

## 🚀 Quick start

```bash
git clone <this-repo>
cd farm-navigators-space-apps-prep
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/fetch_power_daily.py --lat 10.03 --lon 105.78 --start 20240101 --end 20241231
```

## ✅ Preparation checklist

- [ ] Read the official challenge page and linked resources
- [ ] Everyone creates a free [NASA Earthdata](https://urs.earthdata.nasa.gov/) account
- [ ] Run the POWER example script successfully
- [ ] Explore SMAP / GPM / MODIS in [Worldview](https://worldview.earthdata.nasa.gov/)
- [ ] Review existing tools (see `docs/04-existing-solutions.md`)
- [ ] Shortlist 3 ideas and score them (`docs/05-ideas.md`)
- [ ] Pick tech stack and split roles
- [ ] Draft pitch/storyline skeleton

## 📚 Links

See [`docs/03-data-access-guide.md`](docs/03-data-access-guide.md) for all data portals and APIs.

## 📄 License

MIT – see [LICENSE](LICENSE).
