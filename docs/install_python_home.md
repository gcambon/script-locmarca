### Install the workshop Python environment on your own computer

During the workshop you work on Kabre, where everything is already installed (the **`psf2026`** kernel, see [Python environment](python_env.md)). After the workshop, you can install the **same packages** on your own laptop and keep using the notebooks, with no cluster.

> [!NOTE]
> **What you need:** about 5 GB of free disk space for the environment (plus the data, see step 7), an internet connection, and 20–30 minutes. You do **not** need administrator rights.

**The plan, in 7 steps:**

1. Install **Miniforge** (the tool that installs Python and its packages)
2. Download the course material
3. Create the `psf2026` environment
4. Check that it works
5. Open the notebooks in JupyterLab
6. Log in to Copernicus Marine
7. Get some data

---

#### 1. Install Miniforge

[Miniforge](https://github.com/conda-forge/miniforge) gives you the **`mamba`** command, which installs Python packages from **conda-forge**, a free collection of scientific packages. We use `mamba` on this page: it does the same job as the better-known `conda` (also included in Miniforge), but much faster. Use Miniforge rather than Anaconda: it is free for everyone (Anaconda has license limits for institutions), it comes with `mamba`, and it uses conda-forge by default, where all our packages are.

> [!TIP]
> If you already have Anaconda or Miniconda, you can keep it: add `mamba` once with `conda install -n base -c conda-forge mamba`, then go to step 2. (Or replace `mamba` by `conda` in all the commands below: it works too, only slower.)

<details>
<summary><b>Windows</b></summary>

Two options:

- **Option A — simple: plain Windows.** Download and run `Miniforge3-Windows-x86_64.exe` from the [Miniforge page](https://github.com/conda-forge/miniforge#download). Keep the default choices ("Just me"). Then open **Miniforge Prompt** from the Start menu: you type all the commands of this page in that window.
  You get everything **except `cdo` and `ncview`**, which do not exist for Windows. All the Python parts of the notebooks work; only the CDO cells of TP1b do not.

- **Option B — complete: WSL (Linux inside Windows).** Open *PowerShell* as administrator and run `wsl --install`, restart the computer, then open **Ubuntu** from the Start menu and follow the **Linux** instructions below. You get everything, including `cdo` and `ncview`.

</details>

<details>
<summary><b>macOS and Linux</b></summary>

Open a terminal (macOS: *Applications → Utilities → Terminal*) and run:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Answer `yes` to the license, keep the proposed folder (press *Enter*), and answer **`yes`** to the last question (*"initialize Miniforge3?"*). Then **close the terminal and open a new one**.

</details>

Check that it worked: the command below prints a version number.

```bash
mamba --version
```

#### 2. Download the course material

With git (macOS, Linux, WSL; on Windows install [Git for Windows](https://git-scm.com/download/win) first):

```bash
cd ~
git clone https://github.com/gcambon/script-locmarca.git
cd script-locmarca
```

No git? On <https://github.com/gcambon/script-locmarca>, click **Code → Download ZIP**, unzip it, and go into the folder with `cd`.

#### 3. Create the `psf2026` environment

From the `script-locmarca` folder (it contains the file `environment.yml`, the list of packages):

```bash
# macOS, Linux, WSL
mamba env create -f environment.yml

# plain Windows (Miniforge Prompt)
mamba env create -f environment_windows.yml
```

This downloads and installs all the packages: it can take **up to 30 minutes**, even if the screen looks stuck for a while. Be patient: it is done only once.

Then **activate** the environment. Do this **every time** you open a new terminal:

```bash
mamba activate psf2026
```

The start of the prompt changes from `(base)` to `(psf2026)`.

#### 4. Check that it works

```bash
python -c "import xarray, cartopy, cmocean, copernicusmarine; print('Python packages: OK')"
ncks --version
cdo --version        # not on plain Windows
```

✅ **Check:** `Python packages: OK`, then two version numbers, and no `ModuleNotFoundError` or `command not found`.

#### 5. Open the notebooks in JupyterLab

```bash
cd ~/script-locmarca
mamba activate psf2026
jupyter lab
```

JupyterLab opens in your web browser. Open a notebook, for example `Session01/01a_basics_xarray_EN.ipynb`: since JupyterLab was started from the `psf2026` environment, the default kernel (**Python 3**) is the right one.

As on Kabre, work in your own copy of each notebook (`..._EN_mine.ipynb`, see [Hands-on sessions](handson_session.md)).

<details>
<summary>🚀 Optional: use the environment in VS Code, or give it a name in Jupyter</summary>

To see the environment as **psf2026** in the kernel list (useful in VS Code, or if you have several environments):

```bash
mamba activate psf2026
python -m ipykernel install --user --name psf2026 --display-name "psf2026"
```

In VS Code (with the *Python* and *Jupyter* extensions): open the `script-locmarca` folder, open a notebook, click **Select Kernel** (top right) and choose **psf2026**.

</details>

#### 6. Log in to Copernicus Marine

To download data yourself (TP2a), log in once with your free [Copernicus Marine account](https://data.marine.copernicus.eu/register):

```bash
mamba activate psf2026
copernicusmarine login
```

Type your username and password: they are saved on your computer, so you do not have to do it again.

#### 7. Get some data

The notebooks look for the data **first on Kabre**, then in the folder `data/DATASETS_PSF/` of the course material:

```python
OBS_DIR = "/data/gcambon/COMMONDATA/DATASETS_PSF/"
if not Path(OBS_DIR).exists():          # not on Kabre
    OBS_DIR = "../data/DATASETS_PSF"
```

So put the data in `script-locmarca/data/DATASETS_PSF/`, keeping the same sub-folders (`COSTARICA_DS/`, `GLOBAL_DS/`, `MODEL_DS/`). Two ways:

- **Copy it from Kabre before the end of the workshop**, while your account is still open (Friday: *copy of the data you want to keep*). The whole set is about **16 GB**: copy only what you need. For example, the Costa Rica files (≈ 4 GB), from a terminal **on your own computer**:

  ```bash
  mkdir -p ~/script-locmarca/data/DATASETS_PSF
  scp -r taller-locmarcaXXX@kabre.cenat.ac.cr:/data/gcambon/COMMONDATA/DATASETS_PSF/COSTARICA_DS ~/script-locmarca/data/DATASETS_PSF/
  ```

  (Replace `taller-locmarcaXXX` with your account. On Windows, MobaXterm also lets you drag and drop files from Kabre.)

- **Download your own data** with the Copernicus Marine toolbox, as in TP2a, for your region and your period.

---

#### If something goes wrong

| Problem | What to do |
|---|---|
| `mamba: command not found` | Close the terminal and open a new one. On Windows, use **Miniforge Prompt**, not the normal command prompt. |
| `mamba activate` says the shell is not initialized | Run `mamba shell init` once, then close the terminal and open a new one. (`conda activate psf2026` also works: it does exactly the same.) |
| `ModuleNotFoundError: No module named 'xarray'` in a notebook | The notebook does not use the `psf2026` environment: start `jupyter lab` **after** `mamba activate psf2026`, or choose the **psf2026** kernel. |
| `FileNotFoundError` on a `.nc` file | The data is not in `data/DATASETS_PSF/` (step 7), or not in the right sub-folder. |
| `cdo: command not found` on Windows | Normal on plain Windows: use WSL (step 1, option B), or do the same computation in Python. |
| An error while downloading packages (proxy, firewall) | Try from another network (at home rather than at the institute), or ask your IT service. |

Other useful commands:

```bash
mamba env list                                      # list your environments
mamba env update -f environment.yml --prune         # update psf2026 after a change of environment.yml
mamba env remove -n psf2026                         # delete the environment (frees the disk space)
```

See also the Copernicus Marine guide [How to create a local Python environment for your Copernicus Marine projects](https://help.marine.copernicus.eu/en/articles/6000911-how-to-create-a-local-python-environment-for-your-copernicus-marine-projects).
