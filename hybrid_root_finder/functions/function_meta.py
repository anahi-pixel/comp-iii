from dataclasses import dataclass
from typing import Callable

from point import Point


@dataclass
class ContinuousFunctionMeta:
    name: str = ""
    context: str = ""


@dataclass
class ContinuousFunction:
    meta: ContinuousFunctionMeta
    function: Callable
    boundaries: list[Point] = None

    def __post_init__(self):
        if self.boundaries is not None:
            self.function = self.function(self.boundaries)
