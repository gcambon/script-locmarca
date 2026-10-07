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
- in the JupyterLab file browser, right-click the notebook → **Duplicate**;
- rename the copy, e.g. `01b_explore_nco_cdo_EN_mine.ipynb` (right-click → **Rename**);
- open the `_mine` copy and work only there.

Your `_mine` copies are never touched by `git pull`.

The notebooks of each session, and the order to follow, are listed in [Session01](../Session01/README.md) and [Session02](../Session02/README.md).

#### If `git pull` fails

If `git pull` says that *your local changes would be overwritten*, you have edited an original notebook. Keep your work, then restore the original:

```bash
cd $HOME/script-locmarca
cp Session01/01b_explore_nco_cdo_EN.ipynb Session01/01b_explore_nco_cdo_EN_mine.ipynb   # keep your work (adapt the name)
git checkout -- Session01/01b_explore_nco_cdo_EN.ipynb                                   # restore the original
git pull
```

If you are not sure, ask a trainer before typing anything.
