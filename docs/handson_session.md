### Hands-on sessions

#### 1. Get the latest version of the material

Before each session, in a terminal:

```bash
cd $HOME/script-locmarca
git pull
```

#### 2. Work in your own copy of each notebook

**Never edit the original notebooks** (for example `Session01/01b_explore_nco_cdo_EN.ipynb`): the trainers may update them during the week, and `git pull` would then fail.

For each notebook, make your own copy, with `_mine` at the end of its name:
- in the JupyterLab file browser, right-click the notebook → **Duplicate**: JupyterLab creates a copy named `…-Copy1.ipynb`;
- rename this copy, e.g. `01b_explore_nco_cdo_EN_mine.ipynb` (right-click → **Rename**);
- open the `_mine` copy, select the **`psf2026`** kernel (top right), and work only there.

Your `_mine` copies are never touched by `git pull`. The files you create (figures, netCDF files in the `data_tp…/` folders) are not touched either.

#### 3. Which notebooks, in which order

| Session | Notebooks |
|---|---|
| [Session01](../Session01/README.md) | TP1a (xarray basics), then TP1b (observations already on Kabre, NCO/CDO) |
| [Session02](../Session02/README.md) | TP2a (getting data from Copernicus), TP2b (biogeochemistry), TP2c (climatology vs interannual variability) |
| [Session03](../Session03/README.md) | TP3 (ocean model outputs) |

Each session folder has its own page with the order, the duration and the data used.

#### If `git pull` fails

If `git pull` says that *your local changes would be overwritten*, you have edited an original notebook. Keep your work, then restore the original:

```bash
cd $HOME/script-locmarca
cp Session01/01b_explore_nco_cdo_EN.ipynb Session01/01b_explore_nco_cdo_EN_mine2.ipynb   # keep your work (adapt the names)
git checkout -- Session01/01b_explore_nco_cdo_EN.ipynb                                    # restore the original
git pull
```

Use a new name for the copy (here `_mine2`), so that you do not overwrite a `_mine` copy you already have.

If you are not sure, ask a trainer before typing anything.
