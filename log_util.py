"""A small buffered file logger."""

import time
from typing import List

LOG_LINES: List[str] = []
DEBUG = False


def log(message: str) -> None:
    """Append and print a timestamped log message."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def debug(message: str) -> None:
    """Log a debug message when debugging is enabled."""
    if DEBUG:
        log(f"DEBUG: {message}")


def flush_log(path: str) -> None:
    """Append buffered messages to a file, then clear the buffer."""
    with open(path, "a", encoding="utf-8") as log_file:
        for line in LOG_LINES:
            log_file.write(f"{line}\n")
    LOG_LINES.clear()
