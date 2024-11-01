from typing import Any


def mean(args):
    """Prints the mean."""
    m = sum(args) / len(args)
    print("mean :", m)


def median(args):
    """Prints the median."""
    args_list = list(args)
    args_list.sort()
    middle_index = len(args_list) // 2
    if len(args_list) % 2 == 1:
        print("median :", args_list[middle_index])
    else:
        print("median :", (args_list[middle_index - 1]
              + args_list[middle_index]) / 2)


def quartile(args):
    """Prints the quartile with Nearest Rank Method."""
    data = list(args)
    data.sort()
    n = len(args)
    q1 = (n + 1) / 4
    q3 = 3 * ((n + 1) / 4)
    q1 = int(q1) - 1
    q3 = int(q3) - 1
    print("quartile :", [data[q1], data[q3]])


def std(args):
    """Prints the standard deviation of the population."""
    m = sum(args) / len(args)
    s = sum([(x - m)**2 for x in args])
    s = (s / len(args))**0.5
    print("std :", s)


def var(args):
    """Prints the variance of the population."""
    m = sum(args) / len(args)
    s = sum([(x - m)**2 for x in args])
    s = (s / len(args))**0.5
    s_squared = s**2
    print("var :", s_squared)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Prints statistic values according to kwargs."""
    # Check if elements are numbers
    if any([True if not (type(element) is int or type(element) is float)
            else False for element in args]):
        print("ERROR")
        exit()

    # Print the statistics
    for statistic in kwargs.values():
        # Check if tuple is empty
        if len(args) == 0:
            print("ERROR")
            continue

        # Print out statistic
        if statistic == "mean":
            mean(args)
        elif statistic == "median":
            median(args)
        elif statistic == "quartile":
            quartile(args)
        elif statistic == "std":
            std(args)
        elif statistic == "var":
            var(args)
