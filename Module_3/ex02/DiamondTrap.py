from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    "King class inherits from Baratheon and Lannister."
    def set_eyes(self, color):
        "Set eye color."
        self.eyes = color

    def get_eyes(self):
        "Get eye color."
        return self.eyes

    def set_hairs(self, color):
        "Set hair color."
        self.hairs = color

    def get_hairs(self):
        "Get hair color."
        return self.hairs
