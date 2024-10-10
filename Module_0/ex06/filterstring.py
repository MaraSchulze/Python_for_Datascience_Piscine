import sys
from ft_filter import ft_filter


def main():
    """returns all words in a string that are longer than N characters.
        S contains only letters and spaces, N is an int.
    """

    args = sys.argv

    # if there are not 2 arguments
    if len(args) != 3:
        print("AssertionError: the arguments are bad")
        exit()

    # if second argument is not an int
    try:
        N = int(args[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        exit()

    S = args[1]

    # if first argument does not consist of letters or spaces
    temp = [c for c in S if c.isalnum() or c.isspace()]
    if len(temp) != len(S):
        print("AssertionError: the arguments are bad")
        exit()

    # filter
    result = list(ft_filter(lambda x: len(x) > N, S.split(" ")))
    print(result)


if __name__ == "__main__":
    main()
