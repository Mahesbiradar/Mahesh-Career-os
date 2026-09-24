class Student:

    college = "ABC"

    def __init__(self, name):
        self.name = name

s1 = Student("A")
s2 = Student("B")

s1.college = "XYZ"

print(s1.college)
print(s2.college)