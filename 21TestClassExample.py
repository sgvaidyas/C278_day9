class Emp:
    myemp = []
    def setdata(self):
        self.id = int(input("Enter id = "))
        self.name = input("Enter the name = ")
        Emp.myemp.append(self)

    def __str__(self):
        return str(self.id) + " = " +self.name

e1 = Emp()
e1.setdata()
e2 = Emp()
e2.setdata()
for x in Emp.myemp:
    print(x)




