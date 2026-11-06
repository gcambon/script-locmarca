"""Empty the data_tp*/ folders created by the TP notebooks (Session*/data_tp1, data_tp2, data_tp3...).

These folders hold the files the notebooks write or download (figures, netCDF files).
The folders themselves are kept (the notebooks recreate them anyway), and so is a
.gitkeep file if there is one. Nothing else in the repository is touched.

The script first lists what it will delete and asks for confirmation.

⚠️ Instructor tool: the students need their data_tp2/ files for the Thursday mini-project.

Usage:
  python clean_data.py                   # every Session*/data_tp*/
  python clean_data.py Session02         # only the data_tp* folders of Session02
  python clean_data.py --dry-run         # only list, delete nothing
  python clean_data.py --yes             # no confirmation question
"""
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KEEP = {".gitkeep"}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("sessions", nargs="*", metavar="SessionXX",
                        help="optional: only clean these sessions, e.g. 'Session02' or 'Session01 Session02' "
                             "(nothing = all sessions)")
    parser.add_argument("--dry-run", action="store_true", help="only list what would be deleted")
    parser.add_argument("--yes", action="store_true", help="delete without asking")
    args = parser.parse_args()

    sessions = [ROOT / s for s in args.sessions] if args.sessions else sorted(ROOT.glob("Session*"))
    for s in sessions:
        if not s.is_dir():
            sys.exit(f"✗ {s}: no such folder")
    folders = sorted(d for s in sessions for d in s.glob("data_tp*") if d.is_dir())

    to_delete = [p for d in folders for p in sorted(d.iterdir()) if p.name not in KEEP]
    if not to_delete:
        print("Nothing to delete: the data_tp* folders are already empty.")
        return

    def size(p):
        return p.stat().st_size if p.is_file() else sum(f.stat().st_size for f in p.rglob("*") if f.is_file())

    total = 0
    for p in to_delete:
        total += size(p)
        print(f"  {size(p) / 1e6:8.1f} MB  {p.relative_to(ROOT)}{'/' if p.is_dir() else ''}")
    print(f"{len(to_delete)} items, {total / 1e6:.1f} MB in {', '.join(str(d.relative_to(ROOT)) for d in folders)}")

    if args.dry_run:
        print("Dry run: nothing deleted.")
        return
    if not args.yes and input("Delete them? [y/N] ").strip().lower() not in ("y", "yes"):
        print("Cancelled: nothing deleted.")
        return

    for p in to_delete:
        if p.is_dir() and not p.is_symlink():
            shutil.rmtree(p)
        else:
            p.unlink()
    print(f"✓ Deleted {len(to_delete)} items ({total / 1e6:.1f} MB).")


if __name__ == "__main__":
    main()
