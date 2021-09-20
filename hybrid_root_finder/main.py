from approximate import FunctionApproximation
from functions import FUNCTIONS
from dataclasses import dataclass


@dataclass
class Params:
    function: int
    interval: list[float] = None
    constants: list[float] = None

    def __post_init__(self):
        f = FUNCTIONS[self.function]
        if self.interval is None:
            self.interval = f.interval
        if self.function < 3 and self.constants is None:
            self.constants = f.constants


def get_args(args: list[str]):
    if len(args) < 1:
        function_index = 0
    else:
        function_index = int(args[0])

    args = [
            float(i)
            for i in args[1:]
        ]

    consts = None
    interval = None

    if len(args) == 2:
        interval = args
    elif len(args) > 2:
        a, b, consts = args
        interval = [a, b]

    return Params(function_index, interval, consts)


def main(params: Params) -> None:
    function = FUNCTIONS[params.function]

    print(function.meta.name)
    print()
    print(function.meta.context)
    print()
    print('> Calculating...')

    approx = FunctionApproximation.dekkerMethod(
        function.function(*params.constants),
        *params.interval
        )

    print('> Done!')
    print()

    print('For the interval:', tuple(params.interval))
    print('Dekker method found a zero at:', approx)


if __name__ == '__main__':
    import sys

    main(get_args(sys.argv[1:]))
