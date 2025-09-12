from __future__ import annotations
from datetime import datetime
from typing import Protocol


DATE_TIME_FORMATTER = "%d-%m-%Y %H:%M:%S"

# Swim Protocol: requires get_duration_of_swim(self, start: datetime, end: datetime) -> datetime.
# Any class with this method conforms (duck typing); no inheritance needed—enables flexible, typed APIs.
class Swim(Protocol):
    def get_duration_of_swim(self, start: datetime, end: datetime) -> datetime:
        pass