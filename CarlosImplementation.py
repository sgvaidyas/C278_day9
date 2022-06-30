class Students:
    def setDetails(self, roll, name, total):
        self.roll = roll
        self.name = name
        self.total = total

    def display(self):
        fp = open("studentRecords.txt", "r")
        for line in fp.readlines():
            print(line)

    def writeRecord(self):
        fp = open("studentRecords.txt", "a")
        fp.write("\nStudent roll: " + self.roll)
        fp.write("\t\tStudent name: " + self.name)
        fp.write("\t\tStudent Total: " + self.total)

flag=True
while flag==True:
    choice = input("Would you like to\n1. Insert Student \n 2. Display Students \n3. Find Student \n4. Exit\n")
    if choice == "1":
        roll = input("What is students roll number: ")
        name = input("What is students name: ")
        total = input("What is students total: ")
        new_student = Students()
        new_student.setDetails(roll,name,total)
        new_student.writeRecord()
        print("Student successfully added")
    elif choice == "2":
        print("Here are all the students")
        Students().display()
    elif choice == "3":
        fp = open("studentRecords.txt","r")
        roll = input("What is the student's Roll Number: ")
        student_Roll = "Student roll: " + roll
        found = False
        for line in fp.readlines():
            if student_Roll in line:
                print(line)
                found = True
        if not found:
            print("Student record not found.")

    else:
        flag=False
