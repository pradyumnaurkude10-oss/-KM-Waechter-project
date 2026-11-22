"""Small helpers for fleet units, formatting, and collections."""

from typing import Iterable, List, Optional, Tuple, TypeVar, Union

# One kilometre is approximately 0.621371 miles.
MILES_PER_KM = 0.621371
Number = Union[int, float]
T = TypeVar("T")


def km_to_miles(km: Number) -> float:
    """Convert kilometres to miles."""
    return km * MILES_PER_KM


def format_number(value: Number) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: Number) -> str:
    """Format a percentage as a whole number."""
    return f"{value:.0f}%"


def mean(values: Iterable[Number]) -> float:
    """Return the arithmetic mean, or zero for an empty iterable."""
    items = list(values)
    return sum(items) / len(items) if items else 0.0


def is_due(pct: Number, threshold: Number) -> bool:
    """Return whether a percentage meets its threshold."""
    return pct >= threshold


def parse_service_date(text: str) -> Optional[Tuple[int, int, int]]:
    """Parse a dotted day-month-year date into year, month, day."""
    parts = text.split(".")
    if len(parts) != 3:
        return None
    day, month, year = (int(part) for part in parts)
    return year, month, day


def chunk_list(items: Iterable[T], size: int) -> List[List[T]]:
    """Split items into consecutive chunks of the requested size."""
    if size <= 0:
        raise ValueError("chunk size must be positive")

    chunks: List[List[T]] = []
    current: List[T] = []
    for item in items:
        current.append(item)
        if len(current) == size:
            chunks.append(current)
            current = []
    if current:
        chunks.append(current)
    return chunks
