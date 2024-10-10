import sys


def print_count(string):
    """Counts letters in string and prints sentence.
    """

    print("The text contains {} characters:".format(len(string)))


def print_upper(string):
    """Counts upper case letters in string and prints sentence.
    """

    upper = [letter for letter in string if letter.isupper()]
    print("{} upper letters".format(len(upper)))


def print_lower(string):
    """Counts lower case letters in string and prints sentence.
    """

    lower = [letter for letter in string if letter.islower()]
    print("{} lower letters".format(len(lower)))


def print_punctuation(string):
    """Counts punctuation marks in string and prints sentence.
    """

    punctuation = [letter for letter in string if letter in "!\"#$%&'()*+,-./:\
        ;<=>?@[\\]^_`{|}~"]
    print("{} punctuation marks".format(len(punctuation)))


def print_spaces(string):
    """Counts whitespaces in string and prints sentence.
    """

    spaces = [letter for letter in string if letter.isspace()]
    print("{} spaces".format(len(spaces)))


def print_digits(string):
    """Counts digits in string and prints sentence.
    """

    digits = [letter for letter in string if letter.isdigit()]
    print("{} digits".format(len(digits)))


def main():
    """Gives a statistic about a string provided on the command line.
    """

    args = sys.argv
    if len(args) > 2:
        print("Assertion Error: More than one argument")
        exit()
    if len(args) == 1 or len(args) == 2 and args[1] == "":
        print("What is the text to count?")
        user_input = sys.stdin.readline()
    else:
        user_input = args[1]

    print_count(user_input)
    print_upper(user_input)
    print_lower(user_input)
    print_punctuation(user_input)
    print_spaces(user_input)
    print_digits(user_input)


if __name__ == "__main__":
    main()
