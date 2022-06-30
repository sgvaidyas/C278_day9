class Student:
    _l=[]
    def setdetails(self, roll, name, total):
        self.roll=roll
        self.name=name
        self.total=total
        s=str(self.roll)+" " +self.name+" " +str(self.total)
        Student._l.append(s)

    def display(self):
        fp=open("students", "r")
        cnt=1
        for line in fp.readlines():
            print(cnt," = " , line,end="")
            cnt+=1
        fp.close()

    def writeRecord(self):
        fp=open("students", "w")
        for x in Student._l:
            fp.write(x+ "\n")
        fp.close()

a=Student()

a.setdetails(3, "a", 11)
a.writeRecord()

a.setdetails(2, "jim", 11)
a.writeRecord()
a.display()









