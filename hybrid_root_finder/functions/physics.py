import math
from typing import Callable

from functions.function_meta import ContinuousFunction, ContinuousFunctionMeta
from point import Point


def testFunction(mass: float, gravity: float) -> Callable[[float], float]:
    def f(x: float) -> float:
        return gravity*x**2 - mass*math.exp(x)

    return f

TEST_FUNCTION = ContinuousFunction(
    ContinuousFunctionMeta(
        "Test function",
        "Function used for testing under normal conditions"
    ),
    testFunction
)

def _fallingBodySpeed(boundaries: list[Point]):
    def fallingBodySpeed(mass: float, gravity: float):
        def f(x: float) -> float:
            return (mass * gravity - math.exp(-x * boundaries[1].x / mass) * (mass * gravity - boundaries[0].y * x)) / x - boundaries[1].y

        return f

    return fallingBodySpeed

FALLING_BODY_SPEED_FUNCTION = ContinuousFunction(
    ContinuousFunctionMeta(
        "Speed of falling body",
        "This models the speed of a falling body under air resistance"
    ),
    _fallingBodySpeed,
    [
        Point(0, 3),
        Point(2, 20)
    ]
)
