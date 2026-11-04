# LOCMARCA 26 — Programme

UNA, Heredia (Costa Rica), 16–20 November 2026 · Material: [https://github.com/gcambon/script-locmarca](https://github.com/gcambon/script-locmarca)

Every day: 9:00–12:00 and 14:00–17:00 (except Monday morning and Friday afternoon).
For each notebook, work in your own `_mine` copy: see [Hands-on sessions](docs/handson_session.md).

---

## Day 1 — Monday

**Morning**
- Welcome and introduction of the participants (1 slide per person, PDF to send before the workshop)
- Presentation of the programme (courses and hands-on sessions)
- Working infrastructure: the Kabre cluster and JupyterHub OnDemand (Kabre accounts)

**Afternoon — TP0: installation**
1. [Connect to JupyterLab on Kabre](docs/connexion_jupyterhub.md) (and install MobaXterm for Windows users, for `ssh -X`)
2. [Download the course material with git](docs/git_tp_course.md)
3. [Set up your bash environment](docs/bash_env.md)
4. [Select the Python environment](docs/python_env.md) (`psf2026` kernel)

---

## Day 2 — Tuesday

**Course 1 — Observation products: in situ vs satellite** ([PDF](Courses/01_course_observation_products.pdf))
- ocean / atmosphere / biogeochemistry
- 2D vs 3D
- spatial and temporal coverage, strengths and limits
- climatology vs interannual variability
- gridded data: what it implies (interpolation and its limits)

**Course 2a — Anatomy of a netCDF file** ([PDF](Courses/02a_course_anatomy_netcdf_file.pdf))

**Course 2b — A short introduction to ncview from the terminal** ([PDF](Courses/02b_course_ncview_Kabre_MobaXterm.pdf))

**[Session 1](Session01/README.md)**
- **TP1a** — [xarray basics](Session01/01a_basics_xarray_EN.ipynb) (~1h30–2h): open a netCDF file, select, average, maps with coastlines, several maps side by side.
- **TP1b** — [Observations already on Kabre](Session01/01b_explore_nco_cdo_EN.ipynb) (~2h30): mean and variability maps, time series (Pacific vs Caribbean), a vertical section of the WOA climatology, then the command-line tools NCO and CDO, and a cross-check of the three methods.

**[Session 2](Session02/README.md)**
- **TP2a** — [Getting the data yourself: Copernicus Marine](Session02/02a_Copernicus_EN.ipynb) (~2h30)
  - Exercise 0: Copernicus Marine account and login
  - Exercise 1: satellite SST L4 (OSTIA) and 3D temperature (ARMOR3D) over Costa Rica, with a cross-check of the two
  - Exercise 2: ocean reanalysis (GLORYS12: temperature, salinity, currents) and wind (the Papagayo jet)
  - 🚀 Advanced: SST over an area of your choice

---

## Day 3 — Wednesday

**[Session 2](Session02/README.md)** (continued)
- **TP2b** — [Climatology vs interannual variability](Session02/02b_interannual_EN.ipynb) (~1h30): 31 years of SST, monthly climatology, anomalies, El Niño and La Niña.
- **TP2c** — [Biogeochemistry](Session02/02c_bgc_EN.ipynb) (~1h15): satellite chlorophyll, nitrate and oxygen from a model (PISCES), the oxygen minimum zone.

**Course 3 — Numerical models** (*slides coming soon*): yesterday the observations, today the models.
- What is a numerical model of the ocean, the atmosphere, the climate?
- Key ideas: spatial resolution, time integration, processes, grid types
- What models are used for (process studies)
- Global vs regional, scenarios, limits
- A short presentation of climate models (e.g. <https://esgf-node.ipsl.upmc.fr/projects/esgf-ipsl/>)

**[Session 3](Session03/README.md)**
- **TP3** — [Ocean model outputs: the CROCO regional model](Session03/03_model_EN.ipynb) (~3h, continued on Thursday)
  - what is different in a model output file (grid, terrain-following levels, time, fill values)
  - 2D fields: sea surface temperature, sea level, surface currents
  - 3D fields: depth of the model levels, a vertical section across the Costa Rica Dome, a horizontal slice at 100 m
  - model vs observations vs reanalysis: CROCO vs OSTIA, CROCO vs GLORYS12

---

## Day 4 — Thursday — Goal: a mini-project

**Morning — TP3** (continued)

**Afternoon — TP4: mini-project** — a simple model–data comparison over an area of your choice
- Choose a region of interest
- Get the data: in situ / satellite / ocean and atmosphere reanalyses / ocean model outputs (TP1, TP2, TP3)
- Validation: compare models and observations
- Seasonal cycle and interannual variability of these data (TP2b)

---

## Day 5 — Friday

- Round table: each participant presents their mini-project in 5 slides
- Wrap-up, and copy of the data you want to keep
