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
