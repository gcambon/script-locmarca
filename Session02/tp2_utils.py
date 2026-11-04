"""Helper functions shared by the TP2 notebooks (02a, 02b, 02c).

Keep this file next to the notebooks (and next to your `_mine` copy). The study box and the
folders are defined in the notebook, then given to the helpers once with setup():
    from tp2_utils import setup, download, show_dataset, base_map
    setup(box=[LON_MIN, LON_MAX, LAT_MIN, LAT_MAX], obs_dir=OBS_DIR, data_dir=DATA_DIR)
"""
import shutil
from datetime import datetime, timezone
from pathlib import Path

import copernicusmarine
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Set by setup(), from the values defined in the notebook
BOX = None          # [lon_min, lon_max, lat_min, lat_max]
DATA_DIR = None     # where the downloads go
BACKUP_DIR = None   # instructor's backup copy on Kabre, used only if a download fails


def setup(box, obs_dir, data_dir):
    # Give the helpers the study box and the folders of the notebook
    global BOX, DATA_DIR, BACKUP_DIR
    BOX = list(box)
    DATA_DIR = Path(data_dir)
    BACKUP_DIR = Path(obs_dir) / "TP2_BACKUP"


def _check_setup():
    # Clear message if the setup cell has not been run (e.g. after restarting the kernel)
    if BOX is None:
        raise RuntimeError("Run the setup cell first (the one with setup(...)), then run this cell again.")


def download(fname, **kwargs):
    # Download a Copernicus Marine subset to DATA_DIR/fname, skip if it already exists
    _check_setup()
    todo = [k for k, v in kwargs.items() if v is ...]
    if todo:
        raise ValueError(f"Complete the TODOs first: {todo}")
    out = DATA_DIR / fname
    if out.exists():
        print(f"✓ {out} already there, download skipped ({out.stat().st_size / 1e6:.1f} MB)")
        return out
    try:
        copernicusmarine.subset(output_directory=str(DATA_DIR), output_filename=fname, **kwargs)
    except Exception as err:
        backup = BACKUP_DIR / fname
        if not backup.exists():
            raise
        print(f"⚠ Download failed ({err}).\n  Using the instructor's backup copy: {backup}")
        shutil.copy(backup, out)
    print(f"✓ {out} ({out.stat().st_size / 1e6:.1f} MB)")
    return out


def show_dataset(dataset_id):
    # Print variables, units and coordinate ranges of a Copernicus Marine dataset
    cat = copernicusmarine.describe(dataset_id=dataset_id, disable_progress_bar=True)
    product = cat.products[0]
    part = product.datasets[0].versions[0].parts[0]
    service = next(s for s in part.services if s.service_name == "arco-geo-series")
    print(f"{product.title}\n  product : {product.product_id}\n  dataset : {dataset_id}\n")
    for var in service.variables:
        print(f"  variable {var.short_name!r:20} units: {var.units:10} ({var.standard_name})")
    print()
    for coord in service.variables[0].coordinates:
        if coord.coordinate_id == "time":
            t0, t1 = (datetime.fromtimestamp(v / 1000, tz=timezone.utc).date()
                      for v in (coord.minimum_value, coord.maximum_value))
            print(f"  time      : {t0} → {t1}")
        elif coord.values:
            print(f"  {coord.coordinate_id:9} : {len(coord.values)} levels, {coord.values[0]} → {coord.values[-1]}")
        else:
            print(f"  {coord.coordinate_id:9} : {coord.minimum_value:.3f} → {coord.maximum_value:.3f}, step {coord.step:.3f}")


def base_map(ax, title="", extent=None):
    # extent = [lon_min, lon_max, lat_min, lat_max], the Costa Rica box by default
    if extent is None:
        _check_setup()
    ax.set_extent(extent or BOX, crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND.with_scale("50m"), facecolor="#d4c9a8", zorder=2)
    ax.add_feature(cfeature.COASTLINE.with_scale("50m"), linewidth=0.6, zorder=3)
    ax.add_feature(cfeature.BORDERS.with_scale("50m"), linewidth=0.4, linestyle="--", zorder=3)
    gl = ax.gridlines(draw_labels=True, linewidth=0.3, color="gray", alpha=0.5, linestyle="--")
    gl.top_labels = False
    gl.right_labels = False
    if title:
        ax.set_title(title, fontsize=11)
    return ax
