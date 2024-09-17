class Employee:
    def __init__(self,name):
        self.name=name

class Dancer:
    def __init__(self,dance):
            self.dance=dance
           

class DancerEmployee(Employee, Dancer):
    def __init__(self,dance,name):
            Employee.__init__(self,name)
            Dancer.__init__(self,dance)

    def show(self):
         print(f"{self.name} {self.dance}")

o = DancerEmployee("Kathak", "Shivan")

print(o.name, o.dance)
o.show()
print(DancerEmployee.mro())