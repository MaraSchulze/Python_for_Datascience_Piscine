from abc import ABC, abstractmethod


class Character(ABC):
    """Character class."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Inits first_name and is_alive."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kills character."""
        pass


class Stark(Character):
    """Stark class, inherits from abstract Character."""
    def die(self):
        """Inherits from abstract method die."""
        self.is_alive = False
