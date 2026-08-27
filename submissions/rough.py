class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_default():
        return Employee("Unknown")

    @classmethod
    def create(cls, name):
        return cls(name)


e1 = Employee.create_default()
e2 = Employee.create("Mahesh")

print(e1.name)
print(e2.name)
print(type(e1).__name__)
print(type(e2).__name__)
