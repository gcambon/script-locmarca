# LOCMARCA 26 — Programme

**[MEMO_LOCMARCA](https://docs.google.com/presentation/d/10F9j7Rs2w9Qow3FKAotAXs_TwVafaS9YMexGHde1mmg/edit?usp=sharing)**

16–20 November 2026 · Material: [https://github.com/gcambon/script-locmarca](https://github.com/gcambon/script-locmarca)

Every day: 9:00–12:00 and 14:00–17:00.
For each notebook, work in your own `_mine` copy: see [Hands-on sessions](docs/handson_session.md).

## Day 1 — Monday
  <!-- **Morning** -->
- Welcome and introduction of the participants (1 slide per person, PDF to send before the workshop)
  <!-- - Presentation of the programme (courses and hands-on sessions)
  - Working infrastructure: the Kabre cluster and JupyterHub OnDemand (Kabre accounts) -->
- **TP0**: installation
  - [Connect to JupyterLab on Kabre](docs/connexion_jupyterhub.md) (and install MobaXterm for Windows users, for `ssh -X`)
  - [Download the course material with git](docs/git_tp_course.md)
  - [Set up your bash environment](docs/bash_env.md)
  - [Select the Python environment](docs/python_env.md) (`psf2026` kernel)

- **Course 1 — Observation products: in situ vs satellite**  ([PDF](Courses/01_course_observation_products.pdf))  

- **Course 0a — Anatomy of a netCDF file** ([PDF](Courses/00a_course_anatomy_netcdf_file.pdf))
- **Session01 / TP1a** — [xarray basics](Session01/01a_basics_xarray_EN.ipynb): open a netCDF file, select, average, maps with coastlines, several maps side by side.

- **Course 0b — A short introduction to ncview from the terminal** ([PDF](Courses/00b_course_ncview_Kabre_MobaXterm.pdf))


## Day 2 — Tuesday
  <!-- **Morning** -->
- **Session01 / TP1b** — [Observations already on Kabre](Session01/01b_explore_nco_cdo_EN.ipynb): mean and variability maps, time series (Pacific vs Caribbean), a vertical section of the WOA climatology, then the command-line tools NCO and CDO, and a cross-check of the three methods.

- **Session02 / TP2a** — [Getting the data yourself: Copernicus Marine](Session02/02a_Copernicus_EN.ipynb): Create your Copernicus Marine account, then download and plot satellite SST, 3D temperature (observations and ocean reanalysis) and wind.
  <!-- **Afternoon** -->

- **Session02 / TP2b** — [Climatology vs interannual variability](Session02/02b_interannual_EN.ipynb): 31 years of SST, monthly climatology, anomalies, El Niño and La Niña.

- **Session02 / TP2c** — [Biogeochemistry](Session02/02c_bgc_EN.ipynb): satellite chlorophyll, nitrate and oxygen from a model (PISCES), the oxygen minimum zone.

## Day 3 — Wednesday
  <!-- **Morning** -->
- **Course 2 — Numerical models** ([PDF](Courses/02_course_numerical_models.pdf)): yesterday the observations, today the models.

- **Session03 / TP3a** — [A global ocean model: NEMO at 1°](Session03/03a_nemo_EN.ipynb)

- **Session03 / TP3b** — [Sigma levels: a short look at a regional model, CROCO at ~5 km](Session03/03b_croco_EN.ipynb)


## Day 4 — Thursday — Goal: a mini-project

- **[mini-project](Session04/README.md)**: One region, one process: what satellites see, and what a reanalysis does with it

---
## Day 5 — Friday

- Round table: each participant (or pair) presents their mini-project in 5 slides
- Wrap-up, and copy of the data you want to keep
