from typing import Any


def callLimit(limit: int):
    """Example of a decorator. Limits the calls of function to limit."""
    count = 0

    def callLimiter(function):
        def limit_fun(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None
        return limit_fun

    return callLimiter
