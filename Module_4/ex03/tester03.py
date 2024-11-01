from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

# Should raise an error
student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
