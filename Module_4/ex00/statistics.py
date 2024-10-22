from typing import Any


def mean(args):
    "Print mean"
    
    if len(args) == 0:
        print("ERROR")
        return
    
    print("mean : ", end="")
    m = sum(args) / len(args)
    print(m)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    "prints statistic values according to kwargs"


    # Check if elements are numbers
    if any([True if not (type(element) is int or type(element) is float) else False for element in args]):
        print("ERROR")
        exit()

    # Print the statistic
    for statistic in kwargs.values():
        if statistic == "mean":
            mean(args)
        elif statistic == "median":
            # median(args)
            pass
        elif statistic == "quartile":
            pass
