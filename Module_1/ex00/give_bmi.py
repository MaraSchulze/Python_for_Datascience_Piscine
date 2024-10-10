import numpy as np


def check(ls: list):
    """
    Checks if all elements in the list are int or float.
    """

    return all([isinstance(x, (int, float)) for x in ls])


def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    """
    Takes 2 lists with weights and heights and returns a list of BMIs.
    """

    # Check for correct parameter types
    if (not isinstance(height, list) or not isinstance(weight, list) or
       len(height) != len(weight) or
       check(height) is False or check(weight) is False):
        print("Error in parameters")
        exit()

    # Converse into array
    heights = np.array(height)
    weights = np.array(weight)

    # Apply function
    result = weights / heights**2

    return result.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Takes a list of BMIs and a limit, and returns a list of Bools that
    indicate if the BMI is below that limit.
    """

    # Check for correct parameter types
    if check(bmi) is False or not isinstance(limit, int):
        print("Error in parameters")
        exit()

    # Convert into array
    bmis = np.array(bmi)

    # Apply function
    result = bmis > float(limit)

    return result.tolist()
