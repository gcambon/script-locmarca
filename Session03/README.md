# Session 3 — Ocean model outputs: global vs regional

For each notebook, first make your own `_mine` copy (see [Hands-on sessions](../docs/handson_session.md)) and select the `psf2026` kernel.

| Order | Notebook | What you do |
|---|---|---|
| 1 | `03a_nemo_EN.ipynb` (TP3a) | Global model NEMO at 1°: what is in a global model file (longitudes 0–360, model calendar), a global map and a zoom on Costa Rica, El Niño seen from the whole Pacific (Niño 3.4 vs our box), z-levels, sections across the Costa Rica Dome and along the equator |
| 2 | `03b_croco_EN.ipynb` (TP3b) | A short look at a regional model, CROCO (~5.5 km), focused on **sigma levels**: where is the depth in the file, sigma levels vs the z-levels of NEMO, a section across the Costa Rica Dome, a map at 100 m by vertical interpolation |

**The common thread**: the two models differ in their **domain** (global vs regional, 1° vs ~5.5 km) and in their **vertical levels** (z-levels at fixed depths vs sigma levels that follow the sea floor). Each notebook ends with the same recap table, filled in for NEMO in TP3a and for CROCO in TP3b.

**When**: Thursday morning, 9:00–12:00 (TP3a, break, TP3b).

**Data**: the files are already on Kabre (NEMO 4.2-PISCES outputs, CROCO outputs for 1–3 December 2023 and the model grid, plus the GLORYS file of TP2a for an advanced track). Nothing to download.

**Keep your `_mine` copies in this folder**: the notebooks use `croco_helpers.py` (helper functions), which must stay next to them.

**Before**: Course 2 (numerical models), TP1 and TP2.
