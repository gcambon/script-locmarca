# LOCMARCA 26 — Programme

UNA, Heredia (Costa Rica), 16–20 November 2026 · Material: [https://github.com/gcambon/script-locmarca](https://github.com/gcambon/script-locmarca)

Every day: 9:00–12:00 and 14:00–17:00 (except Monday morning and Friday afternoon).
For each notebook, work in your own `_mine` copy: see [Hands-on sessions](docs/handson_session.md).

## Day 1 — Monday
**Morning**
- Welcome and introduction of the participants (1 slide per person, PDF to send before the workshop)
- Presentation of the programme (courses and hands-on sessions)
- Working infrastructure: the Kabre cluster and JupyterHub OnDemand (Kabre accounts)

**Afternoon**
- TP0: installation
  - [Connect to JupyterLab on Kabre](docs/connexion_jupyterhub.md) (and install MobaXterm for Windows users, for `ssh -X`)
  - [Download the course material with git](docs/git_tp_course.md)
  - [Set up your bash environment](docs/bash_env.md)
  - [Select the Python environment](docs/python_env.md) (`psf2026` kernel)

- **Course 0a — Anatomy of a netCDF file** ([PDF](Courses/00a_course_anatomy_netcdf_file.pdf))

- **Course 0b — A short introduction to ncview from the terminal** ([PDF](Courses/00b_course_ncview_Kabre_MobaXterm.pdf))


## Day 2 — Tuesday
**Morning**
- **Course 1 — Observation products: in situ vs satellite**  ([PDF](Courses/01_course_observation_products.pdf))
  <!-- - ocean / atmosphere / biogeochemistry  
  - 2D vs 3D
  - spatial and temporal coverage, strengths and limits
  - climatology vs interannual variability
  - gridded data: what it implies (interpolation and its limits) -->

**Afternoon**
- **[Session 1](Session01/README.md)**
  - **TP1a** — [xarray basics](Session01/01a_basics_xarray_EN.ipynb): open a netCDF file, select, average, maps with coastlines, several maps side by side.
  - **TP1b** — [Observations already on Kabre](Session01/01b_explore_nco_cdo_EN.ipynb): mean and variability maps, time series (Pacific vs Caribbean), a vertical section of the WOA climatology, then the command-line tools NCO and CDO, and a cross-check of the three methods.

- **[Session 2](Session02/README.md)**
  - **TP2a** — [Getting the data yourself: Copernicus Marine](Session02/02a_Copernicus_EN.ipynb)
  <!-- - Exercise 0: Copernicus Marine account and login
  - Exercise 1: satellite SST L4 (OSTIA) and 3D temperature (ARMOR3D) over Costa Rica, with a cross-check of the two
  - Exercise 2: ocean reanalysis (GLORYS12: temperature, salinity, currents) and wind (the Papagayo jet)
  - 🚀 Advanced: SST over an area of your choice -->

## Day 3 — Wednesday
**Morning**
- **[Session 2](Session02/README.md)** (continued)
  - **TP2b** — [Climatology vs interannual variability](Session02/02b_interannual_EN.ipynb): 31 years of SST, monthly climatology, anomalies, El Niño and La Niña.
  - **TP2c** — [Biogeochemistry](Session02/02c_bgc_EN.ipynb): satellite chlorophyll, nitrate and oxygen from a model (PISCES), the oxygen minimum zone.

**Afternoon**
  - **Course 2 — Numerical models** ([PDF](Courses/02_course_numerical_models.pdf)): yesterday the observations, today the models.
<!-- - What is a numerical model of the ocean, the atmosphere, the climate?
- Key ideas: spatial resolution, time integration, processes, grid types
- What models are used for (process studies)
- Global vs regional, scenarios, limits
- A short presentation of climate models (e.g. <https://esgf-node.ipsl.upmc.fr/projects/esgf-ipsl/>) -->

## Day 4 — Thursday — Goal: a mini-project
**Morning**
- **[Session 3](Session03/README.md)**: ocean model outputs
  - **TP3a** — [A global ocean model: NEMO at 1°](Session03/03a_nemo_EN.ipynb)
  <!-- - a global model file: longitudes from 0 to 360, a model calendar, z-levels
  - a global map, then a zoom on Costa Rica: what a 1° grid can and cannot show near the coast
  - back to the whole Pacific: El Niño seen from where it is born (Niño 3.4 vs the Costa Rica box, 2006–2025)
  - z-levels: fixed depths, a vertical section across the Costa Rica Dome, a map at 100 m, a section along the equator -->
  - **TP3b** — [Sigma levels: a short look at a regional model, CROCO at ~5 km](Session03/03b_croco_EN.ipynb)
  <!-- - where is the depth in a regional model file? (`s_rho`, level 0 at the bottom)
  - sigma levels vs z-levels: CROCO and NEMO along the same section
  - a vertical section across the Costa Rica Dome, a map at 100 m by vertical interpolation -->

**Afternoon** 
- **Session 4** : mini-project — a simple model–data comparison over an area of your choice
<!-- - Choose a region of interest
- Get the data: in situ / satellite / ocean and atmosphere reanalyses / ocean model outputs (TP1, TP2, TP3)
- Validation: compare models and observations
- Seasonal cycle and interannual variability of these data (TP2b) -->

---
## Day 5 — Friday

- Round table: each participant presents their mini-project in 5 slides
- Wrap-up, and copy of the data you want to keep
