# Session 2 — Getting the data yourself: Copernicus Marine

For each notebook, first make your own `_mine` copy (see [Hands-on sessions](../docs/handson_session.md)) and select the `psf2026` kernel.

| Order | Notebook | What you do |
|---|---|---|
| 1 | `02a_Copernicus_EN.ipynb` (TP2a) | Create your Copernicus Marine account, then download and plot satellite SST, 3D temperature (observations and ocean reanalysis) and wind |
| 2 | `02b_interannual_EN.ipynb` (TP2b) | 31 years of SST: climatology, anomalies, El Niño and La Niña |
| 3 | `02c_bgc_EN.ipynb` (TP2c) | Biogeochemistry: satellite chlorophyll, nitrate and oxygen from a model, the oxygen minimum zone |

<!-- TP2b and TP2c are complementary: the trainers will tell you when to do them. -->

**Before you start**: you need a free [Copernicus Marine account](https://data.marine.copernicus.eu/register), and to log in once in a terminal with `copernicusmarine login` (Exercise 0 of TP2a). Create the account **before the session** if you can: the confirmation e-mail can take a while.

**Keep your downloads small**: about 20 people download the same data at the same time, on the same network. **Do not change** the regions and periods given in the notebooks.

**Keep your `_mine` copies in this folder**: the three notebooks import their helper functions from `tp2_utils.py`, which must stay next to them.

**Your files** go to the folder `data_tp2/`, next to the notebooks. **Keep it**: you will reuse these files in the mini-project on Thursday.

**Before**: Course 0a (anatomy of a netCDF file), Course 1 (observation products) and TP1.
