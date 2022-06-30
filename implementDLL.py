from doublyLinedList import DLL
flag=True
ob = DLL.DoublyLinkedList()
while flag==True:
    print("\n1 Insert in the beginning")
    print("2 Insert at the end")
    print("3 Insert at the pos")
    print("4 Delete at the beginning")
    print("5 Delete at the end")
    print("6 Delete at the pos")
    print("7 Display")
    ch = int(input("Enter the choice = "))
    if ch==1:
        ob.insertBegin()
    elif ch==2:
        ob.insertEnd()
    elif(ch==3):
        ob.insertPos()
    elif(ch==4):
        ob.deleteBegin()
    elif(ch==5):
        ob.deleteEnd()
    elif(ch==6):
        ob.deletePos()
    elif ch==7:
        ob.display()
    else:
        flag=False
