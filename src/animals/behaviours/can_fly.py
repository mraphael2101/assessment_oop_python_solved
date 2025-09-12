from typing import Protocol


class CanFly(Protocol):
    def fly(self, altitude: float, speed: float) -> None:
        pass