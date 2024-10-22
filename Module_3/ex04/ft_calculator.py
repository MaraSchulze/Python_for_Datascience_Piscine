from abc import abstractmethod


class calculator:
    "Calculates vector operations."
    @abstractmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        "Calculates the dot product and prints it out."
        V3 = [a * b for a, b in zip(V1, V2)]
        print("Dot product is : ", sum(V3))

    @abstractmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        "Calculates the vector addition."
        V3 = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is : ", V3)

    @abstractmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        "Calculates the vector subtraction."
        V3 = [float(a - b) for a, b in zip(V1, V2)]
        print("Sous Vector is : ", V3)
