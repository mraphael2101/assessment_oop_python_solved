from __future__ import annotations
from datetime import datetime
from typing import Protocol


DATE_TIME_FORMATTER = "%d-%m-%Y %H:%M:%S"


class Swim(Protocol):
    def get_duration_of_swim(self, start: datetime, end: datetime) -> datetime:
        pass