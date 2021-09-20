from dataclasses import dataclass
from typing import Callable

from point import Point


@dataclass
class ContinuousFunctionMeta:
    name: str = ""
    context: str = ""


@dataclass
class ContinuousFunctionBase:
    meta: ContinuousFunctionMeta
    function: Callable


@dataclass
class ContinuousFunction(ContinuousFunctionBase):
    constants: list[float]
    interval: list[float]
    boundaries: list[Point] = None

    def __post_init__(self):
        if self.boundaries is not None:
            self.function = self.function(self.boundaries)
