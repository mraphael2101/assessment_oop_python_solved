from __future__ import annotations

from ..bird import Bird
from ..behaviours.can_fly import CanFly
from ..behaviours.hop import Hop


class Eagle(Bird, Hop, CanFly):
    def fly(self, altitude: float, speed: float) -> None:
        pass