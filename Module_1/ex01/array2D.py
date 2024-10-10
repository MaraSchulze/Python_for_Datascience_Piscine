import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes in a 2D list and returns a slice start:end.
    """

    # Check for correct format
    if (not isinstance(family, list) or not isinstance(start, int) or
       not isinstance(end, int)):
        print("Wrong input types.")
        exit()

    # Check for correct indexes
    try:
        family[start:end]
    except IndexError:
        print("Indexes not in range")
        exit()

    # Check for correct list shape
    if not all([len(x) == len(family[0]) for x in family]):
        print("Wrong list shape.")
        exit()

    # Print old shape
    arr = np.array(family)
    print("My shape is : " + str(arr.shape))

    # Print new shape
    my_slice = arr[start:end]
    print("My new shape is : " + str(my_slice.shape))

    return my_slice.tolist()
