"""Shared definition of the open-data CSV (data/robots.csv).

Used by scripts/merge.py (which writes the file) and scripts/validate.py (which
checks that the committed file still matches data/parts/*.json).
"""

# Column order of data/robots.csv. Mirrors data/SCHEMA.md, so a field is named
# the same in the CSV and in the JSON records. Columns are appended at the end,
# never inserted, so a reader's script keeps working across versions.
#
# Every column is one flat value: a nested record object is exported as the
# single field that carries its headline value, and a list as its entries joined
# with '; '. Nothing is derived except price_latest_*, which picks one dated
# observation the record already holds (see price_latest()).
CSV_COLUMNS = [
    "id", "name", "manufacturer", "country", "category", "locomotion",
    "release_year", "status",
    "length_mm", "width_mm", "height_mm", "weight_kg", "payload_kg",
    "max_speed_mps", "min_speed_mps", "wheel_diameter_mm", "wheel_count",
    "dof", "runtime_h", "battery_wh", "ip_rating",
    "api_support", "sdk_available", "sdk_name", "onboard_compute",
    "compute_detail", "ros_support", "sensors",
    "price_usd", "price_note", "official_url", "summary",
    "sources", "verification", "data_source",
    # Issue #65: the fields added on 2026-11-18 (Korean market, structured
    # compute, developer readiness, safety, dated prices) as flat columns.
    "name_ko", "manufacturer_ko", "kr_distributors",
    "compute_soc", "compute_tops", "compute_memory_gb", "compute_source",
    "ros2_support", "ros2_url", "sdk_url", "sdk_license", "sim_models",
    "safety_standards", "certifications", "safety_pl", "safety_source",
    "price_latest_amount", "price_latest_currency", "price_latest_date",
    "price_latest_kind", "price_latest_source",
]

# Order in which sim_models keys are written, so the same record always produces
# the same cell (the JSON object keeps insertion order, which is not a contract).
SIM_MODEL_KEYS = ["urdf", "mjcf", "usd", "isaac", "mujoco", "gazebo"]


def csv_cell(v):
    """One record value as CSV text. Unknown (None) is an empty cell; booleans
    are true/false; lists keep their order, joined with '; '."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (list, tuple)):
        return "; ".join(str(x) for x in v)
    return str(v)


def price_latest(record):
    """The dated price observation to export as price_latest_*.

    A price is a dated observation, so the newest one is the record's current
    price. Several observations can share that date when the maker states one
    price per variant: the first of those with kind 'list' (the headline price of
    the model) is taken, else the first of them. The other observations, and
    their per-variant notes, stay in data/parts and data/robots.json. No figure
    is averaged, ranged or converted, and KRW is never stored.
    """
    obs = [o for o in (record.get("price_observations") or []) if isinstance(o, dict)]
    if not obs:
        return {}
    newest = max(str(o.get("date") or "") for o in obs)
    same_day = [o for o in obs if str(o.get("date") or "") == newest]
    for o in same_day:
        if o.get("kind") == "list":
            return o
    return same_day[0]


def kr_distributor_names(record):
    """Korean sales channels as their names joined with '; '."""
    names = [d["name"] for d in (record.get("kr_distributors") or [])
             if isinstance(d, dict) and d.get("name")]
    return "; ".join(names) if names else None


def sim_model_keys(record):
    """Published simulation-model keys, in SIM_MODEL_KEYS order, e.g. 'urdf; mjcf'."""
    models = record.get("sim_models") or {}
    keys = [k for k in SIM_MODEL_KEYS if isinstance(models, dict) and k in models]
    return "; ".join(keys) if keys else None


def _flat_values(record):
    """CSV columns that are not a plain record field of the same name."""
    sdk = record.get("sdk") or {}
    if not isinstance(sdk, dict):
        sdk = {}
    latest = price_latest(record)
    return {
        "kr_distributors": kr_distributor_names(record),
        "sdk_url": sdk.get("url"),
        "sdk_license": sdk.get("license"),
        "sim_models": sim_model_keys(record),
        "price_latest_amount": latest.get("amount"),
        "price_latest_currency": latest.get("currency"),
        "price_latest_date": latest.get("date"),
        "price_latest_kind": latest.get("kind"),
        "price_latest_source": latest.get("source"),
    }


def csv_row(record):
    """One record as a CSV row, in CSV_COLUMNS order."""
    flat = _flat_values(record)
    return [csv_cell(flat[k] if k in flat else record.get(k)) for k in CSV_COLUMNS]
