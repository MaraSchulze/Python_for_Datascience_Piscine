import sys

args = sys.argv

if len(args) == 1:
    exit()
if len(args) > 2:
    print("AssertionError: more than one argument is provided")
    exit()

try:
    number = int(args[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit()

print("I'm Even." if number % 2 == 0 else "I'm Odd.")
