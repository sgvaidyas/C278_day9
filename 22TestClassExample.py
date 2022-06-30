class Emp:
    count = 0
    def setdata(self):
        self.id = int(input("Enter id = "))
        self.name = input("Enter the name = ")
        Emp.count+=1

    def __str__(self):
        return str(self.id) + " = " +self.name

e1 = Emp()
e1.setdata()
e2 = Emp()
e2.setdata()
e3 = Emp()
e3.setdata()
print(Emp.count)
print("e1.count",e1.count)
print("e2.count",e2.count)
e2.count=88
print("e2.count",e2.count)
print("e3.count",e3.count)
print("Emp.count = ",Emp.count)



