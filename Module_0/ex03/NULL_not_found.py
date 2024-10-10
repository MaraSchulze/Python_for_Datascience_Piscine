from types import NoneType


def NULL_not_found(object: any) -> int:
    my_type = type(object)

    if object and not (object != object):
        print("Type not found")
        return 1

    if my_type == NoneType:
        output = "Nothing: " + str(object) + " " + str(my_type)
    elif my_type == float:
        output = "Cheese: " + str(object) + " " + str(my_type)
    elif my_type == int:
        output = "Zero: " + str(object) + " " + str(my_type)
    elif my_type == str:
        output = "Empty: " + str(object) + " " + str(my_type)
    elif my_type == bool:
        output = "Fake: " + str(object) + " " + str(my_type)
    else:
        output = ""

    print(output)
    return 0
