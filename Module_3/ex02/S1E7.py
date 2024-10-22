from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Inherits from abstract method die."""
        self.is_alive = False

    def __str__(self):
        """Overwrites the __str__ method"""
        return self.__repr__()

    def __repr__(self):
        """Overwrites the __repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Inherits from abstract method die."""
        self.is_alive = False

    def __str__(self):
        """Overwrites the __str__ method"""
        return self.__repr__()

    def __repr__(self):
        """Overwrites the __repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creates instances of the Lannister class."""
        return cls(first_name, is_alive)
