"""Download SST, SSH and 3D ocean fields from Copernicus Marine over a Costa Rica box.

Same datasets as download_sst.ipynb / download_2d_ocean.ipynb /
download_3d_ocean_bymonth.ipynb, but on a smaller box (same as TP2:
Papagayo + Costa Rica Dome). Output file names match subset_costarica.sh.

Prerequisite (once):  copernicusmarine login

Usage:
  python download_costarica.py                       # everything, 2023-2024, into ./COSTARICA_DS
  python download_costarica.py --out-dir /data0/user/gcambon/DATA/DATASETS_PSF/COSTARICA_DS
  python download_costarica.py --products sst ssh --years 2023
  python download_costarica.py --dry-run             # check the requests, download nothing

Files that already exist are skipped, so the script can be re-run after an interruption.
"""
import argparse
import calendar
from pathlib import Path

import copernicusmarine

# Study box: Pacific coast of Costa Rica
LON_MIN, LON_MAX = -92.0, -80.0
LAT_MIN, LAT_MAX = 4.0, 14.0

SST_DATASET = "METOFFICE-GLO-SST-L4-REP-OBS-SST"      # OSTIA L4, 0.05°, daily
PHY_DATASET = "cmems_mod_glo_phy_my_0.083deg_P1D-m"   # GLORYS12 reanalysis, 1/12°, daily

PHY_3D_VARIABLES = ["thetao", "so", "uo", "vo"]
DEPTH_MIN, DEPTH_MAX = 0, 500


def download(out_file, dry_run, **kwargs):
    """Call copernicusmarine.subset() over the box, unless out_file already exists."""
    if out_file.exists():
        print(f"✓ {out_file.name} already there, skipped.")
        return
    print(f"⬇ {out_file.name} ...")
    copernicusmarine.subset(
        minimum_longitude=LON_MIN,
        maximum_longitude=LON_MAX,
        minimum_latitude=LAT_MIN,
        maximum_latitude=LAT_MAX,
        output_directory=str(out_file.parent),
        output_filename=out_file.name,
        overwrite=False,
        dry_run=dry_run,
        **kwargs,
    )
    if out_file.exists():
        print(f"✓ {out_file.name}  ({out_file.stat().st_size / 1e6:.1f} MB)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out-dir", default="COSTARICA_DS", type=Path)
    parser.add_argument("--years", nargs="+", type=int, default=[2023, 2024])
    parser.add_argument("--products", nargs="+", choices=["sst", "ssh", "3d"], default=["sst", "ssh", "3d"])
    parser.add_argument("--dry-run", action="store_true", help="check the requests without downloading")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Box: lon [{LON_MIN}, {LON_MAX}]  lat [{LAT_MIN}, {LAT_MAX}]  ->  {args.out_dir}")

    for year in args.years:
        start, end = f"{year}-01-01T00:00:00", f"{year}-12-31T23:59:59"

        if "sst" in args.products:
            download(args.out_dir / f"sst_costarica_{year}.nc", args.dry_run,
                     dataset_id=SST_DATASET, variables=["analysed_sst"],
                     start_datetime=start, end_datetime=end)

        if "ssh" in args.products:
            download(args.out_dir / f"ssh_costarica_{year}.nc", args.dry_run,
                     dataset_id=PHY_DATASET, variables=["zos"],
                     start_datetime=start, end_datetime=end)

        if "3d" in args.products:
            # One file per month: keeps each request (and each file) small
            for month in range(1, 13):
                last_day = calendar.monthrange(year, month)[1]
                download(args.out_dir / f"3Docean_costarica_daily_{year}_{month:02d}.nc", args.dry_run,
                         dataset_id=PHY_DATASET, variables=PHY_3D_VARIABLES,
                         minimum_depth=DEPTH_MIN, maximum_depth=DEPTH_MAX,
                         start_datetime=f"{year}-{month:02d}-01T00:00:00",
                         end_datetime=f"{year}-{month:02d}-{last_day}T23:59:59")

    print("\nDone.")


if __name__ == "__main__":
    main()
