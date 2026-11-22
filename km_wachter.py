"""Decide when fleet vehicles need servicing."""

from typing import Mapping, Union

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80
Car = Mapping[str, Union[str, int]]


def wear_percent(km_since_service: int, interval: int) -> float:
    """Return the percentage of the service interval used."""
    return km_since_service / interval * 100


def needs_service(car: Car) -> bool:
    """Return whether a car has reached the service warning threshold."""
    last_service_km = car.get("last_service_km")
    if last_service_km is None:
        return False

    km_since_service = int(car["odometer"]) - int(last_service_km)
    return wear_percent(km_since_service, SERVICE_INTERVAL_KM) >= WARN_AT_PERCENT


def check_fleet(fleet: list[Car]) -> list[str]:
    """Print and return the IDs of cars due for service."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            car_id = str(car["id"])
            flagged.append(car_id)
            print(f"SERVICE DUE: {car_id}")
    return flagged
