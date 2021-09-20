from approximate import FunctionApproximation
from functions import FUNCTIONS


def main(args: list[str]) -> None:
    if len(args) == 0:
        function = FUNCTIONS[0]
        print(function.meta)
        approx = FunctionApproximation.dekkerMethod(
            function.function(1, 10),  # m = 1, g = 10
            -2, 0  # search interval
        )
        print(approx)


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
