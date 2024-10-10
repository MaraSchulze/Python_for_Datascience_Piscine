def all_thing_is_obj(object: any) -> int:
    my_type = type(object)

    if my_type == str:
        output = object + " is in the kitchen : " + str(my_type)
    elif my_type == int:
        output = "Type not found"
    else:
        output = my_type.__name__.capitalize() + " : " + str(my_type)

    print(output)
    return 42
