from S1E7 import Baratheon, Lannister


robert = Baratheon("Robert")
print(robert.__dict__)
print(robert.__str__)
print(robert.__repr__)
print(robert.is_alive)
robert.die()
print(robert.is_alive)
print(robert.__doc__)

print("---")

cersei = Lannister("cersei")
print(cersei.__dict__)
print(cersei.__str__)
print(cersei.is_alive)

print("---")

jaine = Lannister.create_lannister("jaine", True)
print(f"Name : {jaine.first_name, type(jaine).__name__}, \
        Alive : {jaine.is_alive}")
