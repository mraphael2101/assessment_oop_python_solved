from __future__ import annotations
from datetime import datetime

from ..bird import Bird
from ..behaviours.swim import Swim


class Penguin(Bird, Swim):
    def get_duration_of_swim(self, start: datetime, end: datetime) -> datetime:
        return None

