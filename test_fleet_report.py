"""Tests for fleet summary calculations."""

from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars() -> None:
    """Only the nearly worn car should be due."""
    assert fleet_summary(SAMPLE)["due"] == 1


def test_summary_handles_missing_service_reading() -> None:
    """A missing last-service reading must not crash fleet summaries."""
    fleet = [{"id": "VOS-7788", "odometer": 92000}]

    summary = fleet_summary(fleet)

    assert summary["count"] == 1
    assert summary["average_wear"] == 0.0
