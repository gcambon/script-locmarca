"""Helper functions for the TP3 notebook (CROCO model outputs), written with xarray only.

They work on any CROCO grid, regular or curvilinear (2D coordinates, rotation by `angle`,
`Vtransform` 1 or 2). Keep this file next to the notebook (and next to your `_mine` copy).
"""
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

CROCO_TIME_ORIGIN = "2000-01-01"   # model setting, NOT written in the file (see section 1)
FILL = 1e30                        # anything larger is a netCDF fill value, not data


def open_croco(avg_file, grd_file):
    """Open a CROCO output file and fix the three problems seen in section 1."""
    ds = xr.open_dataset(avg_file, decode_times=False, chunks={"time": 1})
    grd = xr.open_dataset(grd_file)
    # Index variables of the dimensions (0, 1, 2…) are not needed and get in the way when moving u/v
    ds = ds.drop_vars(["xi_rho", "eta_rho", "xi_u", "eta_v", "xi_psi", "eta_psi"], errors="ignore")
    grd = grd.drop_vars(["xi_rho", "eta_rho", "xi_u", "eta_u", "xi_v", "eta_v", "xi_psi", "eta_psi"], errors="ignore")
    # The grid file names the u/v dimensions differently from the output file
    grd = grd.rename({"eta_u": "eta_rho", "xi_v": "xi_rho"})
    # 1. Undeclared fill values (9.97e36) on land-only tiles -> NaN
    for name in ds.data_vars:
        if ds[name].dtype.kind == "f":
            ds[name] = ds[name].where(abs(ds[name]) < FILL)
    # 2. Clean grid (coordinates, bathymetry, masks, metrics) from the grid file
    for name in ["lon_rho", "lat_rho", "lon_u", "lat_u", "lon_v", "lat_v",
                 "h", "mask_rho", "mask_u", "mask_v", "pm", "pn", "f", "angle"]:
        ds[name] = grd[name]
    ds = ds.set_coords(["lon_rho", "lat_rho", "lon_u", "lat_u", "lon_v", "lat_v"])
    # Land points -> NaN (each variable with the mask of its own grid points)
    for name in ds.data_vars:
        dims = set(ds[name].dims)
        if {"eta_rho", "xi_rho"} <= dims and not name.startswith("mask"):
            ds[name] = ds[name].where(ds.mask_rho == 1)
        elif {"eta_rho", "xi_u"} <= dims and not name.startswith("mask"):
            ds[name] = ds[name].where(ds.mask_u == 1)
        elif {"eta_v", "xi_rho"} <= dims and not name.startswith("mask"):
            ds[name] = ds[name].where(ds.mask_v == 1)
    # 3. Time: seconds since the model origin -> real dates
    ds["time"] = np.datetime64(CROCO_TIME_ORIGIN) + ds.time.values.astype("timedelta64[s]")
    return ds


def to_rho(u, v, angle):
    """Move u and v from their own C-grid points to the rho-points, then turn them east/north."""
    u, v = u.reset_coords(drop=True), v.reset_coords(drop=True)
    u_rho = (0.5 * (u + u.shift(xi_u=1))).pad(xi_u=(0, 1)).rename(xi_u="xi_rho")    # average of 2 neighbours
    v_rho = (0.5 * (v + v.shift(eta_v=1))).pad(eta_v=(0, 1)).rename(eta_v="eta_rho")
    u_east = u_rho * np.cos(angle) - v_rho * np.sin(angle)       # rotation (angle = 0 on a grid aligned with east/north)
    v_north = u_rho * np.sin(angle) + v_rho * np.cos(angle)
    return u_east, v_north


def depth_levels(ds, zeta):
    """Depth (m, negative) of every rho-level, from the bathymetry h and the sea level zeta."""
    if int(ds.Vtransform) == 2:                                   # standard CROCO setting
        z = zeta + (zeta + ds.h) * (ds.hc * ds.s_rho + ds.h * ds.Cs_rho) / (ds.hc + ds.h)
    else:                                                         # older setting (Vtransform = 1)
        z0 = ds.hc * ds.s_rho + (ds.h - ds.hc) * ds.Cs_rho
        z = z0 + zeta * (1 + z0 / ds.h)
    return z.transpose("s_rho", ...)


def nearest_point(da, lon, lat):
    """Value(s) of da at the grid point closest to (lon, lat), on any grid."""
    dist = (da.lon_rho - lon) ** 2 + (da.lat_rho - lat) ** 2
    return da.isel(dist.argmin(dim=["eta_rho", "xi_rho"]))


def section_lat(da, lat):
    """Section 'along a latitude': in each column of the grid, the row closest to lat."""
    rows = abs(da.lat_rho - lat).fillna(1e9).argmin("eta_rho")
    return da.isel(eta_rho=rows)


def at_depth(da, z, depth):
    """Interpolate each water column of da (levels s_rho, depths z) at a fixed depth (m, negative)."""

    def value_at_depth(z_col, v_col):
        """In one water column: the value at the requested depth (NaN if the column does not reach it)."""
        return np.interp(depth, z_col, v_col, left=np.nan, right=np.nan)

    return xr.apply_ufunc(value_at_depth,
                          z.compute(), da.compute(),                # load the data in memory (one 3D field: small)
                          input_core_dims=[["s_rho"], ["s_rho"]],   # one column = along s_rho
                          vectorize=True)                           # repeat for every grid point


def base_map(ax, title, extent=None):
    """Land, coastlines and grid on a cartopy map (whole model domain by default)."""
    ax.add_feature(cfeature.LAND.with_scale("50m"), facecolor="#d4c9a8", zorder=2)
    ax.add_feature(cfeature.COASTLINE.with_scale("50m"), linewidth=0.7, zorder=3)
    ax.gridlines(draw_labels=True, linewidth=0.3, linestyle="--", color="gray")
    if extent is not None:
        ax.set_extent(extent, crs=ccrs.PlateCarree())
    ax.set_title(title)
