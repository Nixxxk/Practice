class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showData(self):
        print(f"The name of Employee: {self.id} is {self.name}")

e = Employee("Rahul", 45)
e.showData()
g = Employee("Nikhil", 405)
g.showData()