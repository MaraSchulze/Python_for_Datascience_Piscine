def ft_tqdm(lst: range) -> None:
    """
    This function copies a simple version of tqdm.
    """

    if (lst.stop - lst.start) % lst.step == 0:
        allitems = (lst.stop - lst.start) // lst.step
    else:
        allitems = ((lst.stop - lst.start) // lst.step) + 1

    # print 0% line
    print("\r{:>3}%|{:<50}|{}/{}".format(0, "", 0, allitems), end="")

    items = 1
    for elem in lst:
        percent = int((items / allitems) * 100)
        barlength = percent // 2
        bar = (barlength) * "\u2588"

        # print rest of lines
        print("\r{:>3}%|{:<50}|{}/{}".format(percent, bar, items, allitems),
              end="")

        items += 1

        yield elem
