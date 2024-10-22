class calculator:
    "Calculates a vector with a scalar."

    def __init__(self, vector):
        "Initializes a list with parameter vector."
        self.vector = vector

    def __add__(self, object) -> None:
        "Adds object to every element in vector."
        self.vector = [number + object for number in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        "Adds object to every element in vector."
        self.vector = [number * object for number in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        "Adds object to every element in vector."
        self.vector = [number - object for number in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        "Adds object to every element in vector."
        if object == 0:
            print("Error: Division by zero")
            return
        self.vector = [number / object for number in self.vector]
        print(self.vector)
