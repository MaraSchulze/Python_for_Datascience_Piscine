def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x**2


def pow(x: int | float) -> int | float:
    """Returns x to the x."""
    return x**x


def outer(x: int | float, function) -> object:
    """Closure that applies function count times."""
    count = 0

    def inner() -> int | float:
        nonlocal count

        result = x
        for _ in range(count + 1):
            result = function(result)
        count += 1
        return result

    return inner
