from __future__ import annotations


class Hop:
    # @staticmethod defines a class function that gets no self or class object (cls)
    @staticmethod
    def get_avg_hop_height() -> int:
        return 2

    # Default method equivalent
    def get_max_hop_height(self) -> int:
        return 4