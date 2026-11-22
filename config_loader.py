"""Load known settings from the application's configuration file."""

from typing import Dict, Mapping, Optional

SETTINGS_FILE = "settings.cfg"
KNOWN_KEYS = (
    "service_interval_km",
    "warn_at_percent",
    "report_title",
    "history_file",
    "log_file",
    "mileage_unit",
)


def load_settings(path: Optional[str] = None) -> Dict[str, str]:
    """Read recognized key/value settings from a config file."""
    settings: Dict[str, str] = {}
    with open(path or SETTINGS_FILE, encoding="utf-8") as settings_file:
        for raw_line in settings_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = (part.strip() for part in line.split("=", 1))
            if key in KNOWN_KEYS:
                settings[key] = value
    return settings


def get_int(settings: Mapping[str, str], key: str, fallback: int) -> int:
    """Return a setting as an integer, or the fallback if it is missing/invalid."""
    try:
        return int(settings[key])
    except (KeyError, ValueError):
        return fallback


def get_setting(
    settings: Mapping[str, str], key: str, fallback: str = ""
) -> str:
    """Return a setting or its fallback."""
    return settings.get(key, fallback)
