import sys


def main():
    """
    Prints Morse code of a string that is alphanumeric and spaces.
    """

    MORSE = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
        'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
        'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
        'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ',
        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ',
        ' ': '/ '
    }

    # catch wrong argument number
    args = sys.argv
    if len(args) != 2:
        print("AssertionError: the arguments are bad")
        exit()

    string = [c for c in args[1] if c.isalnum() or c.isspace()]

    # catch if string does not consist of alnum chars and spaces
    if len(string) != len(args[1]):
        print("AssertionError: the arguments are bad")
        exit()

    # set string to upper case
    string = [c.upper() for c in string]

    # print Morse code
    result = "".join([MORSE[c] for c in string])
    print("" if result == "" else result[:-1])


if __name__ == "__main__":
    main()
