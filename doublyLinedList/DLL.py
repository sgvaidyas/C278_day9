from doublyLinedList.myNode import *
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertBegin(self):
        ele = int(input("Enter ele = "))
        temp = Node(ele)
        if self.head is None:
            self.head = temp
        else:
            temp.next=self.head
            self.head.prev = temp
            self.head = temp
        self.count +=1

    def insertEnd(self):
        ele = int(input("Enter ele = "))
        temp = Node(ele)
        if self.head is None:
            self.head = temp
        else:
            lastNode = self.head
            while  lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = temp
            temp.prev = lastNode
        self.count +=1

    def insertPos(self):
        pos = int(input("Enter pos = "))
        if(pos<1 or pos>self.count+1):
            print("Invalid pos")
        elif(pos == 1):
            self.insertBegin()
        elif pos==self.count+1:
            self.insertEnd()
        else:
            ele = int(input("Enter ele = "))
            temp = Node(ele)
            cp = self.head
            for i in range(1,pos):
                cp= cp.next
            pp = cp.prev
            pp.next = temp
            temp.prev = pp
            temp.next =cp
            cp.prev = temp
            self.count +=1


    def deleteBegin(self):
        if self.head is None:
            print("List Empty Delete operation cannot be performed ")
        else:
            ptr = self.head
            print("Deleting = ",self.head.data)
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            del ptr
            self.count -=1

    def deleteEnd(self):
        if self.head is None:
            print("delete operation cannot be performed")
        else:
            ptr = self.head
            for i in range (1, self.count):
                ptr = ptr.next
            pp = ptr.prev
            if pp is not None:
                pp.next = None
            else:
                self.head = None
            print("deleting = ",ptr.data)
            del ptr
            self.count -= 1

    def deletePos(self):
        pos = int(input("Enter pos = "))
        if(pos<1 or pos>self.count):
            print("Invalid pos")
        elif(pos == 1):
            self.deleteBegin()
        elif pos==self.count:
            self.deleteEnd()
        else:
            cp = self.head
            #pos = 2 List = 11   22   33
            for i in range(1,pos):
                cp = cp.next
            #pp = 11 cp = 22
            pp = cp.prev
            #connection 11------>33
            pp.next = cp.next
            #connection 33--->11
            cp.next.prev = pp
            print("Delete =  ",cp.data)
            del cp
            self.count -=1



    def display(self):
        if self.head is None:
            print("LIST IS EMPTY")
        else:
            print("LIST ELE = ")
            ptr=self.head
            while ptr is not None:
                print(ptr.data , end=" ")
                ptr = ptr.next

