"""Build and print nightly fleet-health summaries."""

from typing import Mapping, Union

import fleet_utils
from config_loader import get_setting, load_settings
from km_wachter import SERVICE_INTERVAL_KM, needs_service, wear_percent
from log_util import flush_log, log

Car = Mapping[str, Union[str, int]]


def car_wear(car: Car) -> float:
    """Return service-interval wear, or zero when no reading is available."""
    last_service_km = car.get("last_service_km")
    if last_service_km is None:
        return 0.0
    return wear_percent(
        int(car["odometer"]) - int(last_service_km), SERVICE_INTERVAL_KM
    )


def fleet_summary(fleet: list[Car]) -> dict[str, Union[int, float]]:
    """Summarize fleet size, due cars, and mean wear percentage."""
    total_wear = sum(car_wear(car) for car in fleet)
    due = sum(needs_service(car) for car in fleet)
    average = total_wear / len(fleet) if fleet else 0.0
    return {"count": len(fleet), "due": due, "average_wear": average}


def print_report(fleet: list[Car]) -> None:
    """Print and log the nightly fleet report."""
    settings = load_settings()
    log(get_setting(settings, "report_title", "Nightly fleet report"))
    summary = fleet_summary(fleet)
    print(f"Fleet: {summary['count']} cars")
    print(f"Due for service: {summary['due']}")
    print(f"Average wear: {summary['average_wear']:.0f}%")
    total_km = sum(int(car["odometer"]) for car in fleet)
    total_miles = fleet_utils.km_to_miles(total_km)
    print(f"Fleet distance: {fleet_utils.format_number(total_miles)} miles")
    flush_log(get_setting(settings, "log_file", "km_wachter.log"))
