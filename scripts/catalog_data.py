"""Shared definition of the open-data CSV (data/robots.csv).

Used by scripts/merge.py (which writes the file) and scripts/validate.py (which
checks that the committed file still matches data/parts/*.json).
"""

# Column order of data/robots.csv. Mirrors data/SCHEMA.md, so a field is named
# the same in the CSV and in the JSON records.
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
]


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


def csv_row(record):
    """One record as a CSV row, in CSV_COLUMNS order."""
    return [csv_cell(record.get(k)) for k in CSV_COLUMNS]
