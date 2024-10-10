def trueFunction(object):
    return object is True


def ft_filter(func, it):
    """Recodes the inbuilt filter function
    """

    if func is None:
        func = trueFunction

    result = [x for x in it if func(x) is True]

    return iter(result)
