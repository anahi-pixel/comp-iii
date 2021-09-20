from dataclasses import dataclass, field
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


@dataclass
class ContinuousPolarFunction(ContinuousFunctionBase):
    period: float
    interval: list[float] = field(init=False)

    def __post_init__(self):
        self.interval = [0, self.period]
