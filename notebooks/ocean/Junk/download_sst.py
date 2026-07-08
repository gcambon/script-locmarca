"""
Téléchargement SST Amérique Centrale 2023-2024
Copernicus Marine — OSTIA L4 REP (reprocessed)

Prérequis :
    micromamba install -c conda-forge copernicusmarine
    copernicusmarine login
"""

import copernicusmarine
from pathlib import Path

DATA_DIR = Path("data_sst")
DATA_DIR.mkdir(exist_ok=True)

DATASET_ID = "METOFFICE-GLO-SST-L4-REP-OBS-SST"
VARIABLE   = "analysed_sst"

LON_MIN, LON_MAX = -100, -60
LAT_MIN, LAT_MAX =    5,  30

for year in [2023, 2024]:
    out_file = DATA_DIR / f"sst_central_america_{year}.nc"

    if out_file.exists():
        print(f"✓ {out_file} déjà présent, ignoré.")
        continue

    print(f"⬇ Téléchargement {year}...")
    copernicusmarine.subset(
        dataset_id        = DATASET_ID,
        variables         = [VARIABLE],
        minimum_longitude = LON_MIN,
        maximum_longitude = LON_MAX,
        minimum_latitude  = LAT_MIN,
        maximum_latitude  = LAT_MAX,
        start_datetime    = f"{year}-01-01T00:00:00",
        end_datetime      = f"{year}-12-31T23:59:59",
        output_directory  = str(DATA_DIR),
        output_filename   = out_file.name,
        overwrite         = False,
    )
    print(f"✓ {out_file}  ({out_file.stat().st_size / 1e6:.1f} Mo)")

print("\nTerminé.")
