import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(default="", init=False)
    id: str = field(default=0, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
        self.id = generate_id()
