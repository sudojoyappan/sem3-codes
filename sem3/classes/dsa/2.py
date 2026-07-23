class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_first(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
        new.next=self.head
        self.head.prev=new
        self.head=new
    def insert_at_last(self,data):
        new=Node(data)
        itr=self.tail
        itr=itr.prev
        new.prev=itr
        itr.next=new
        self.tail=new
    def printll(self):
        itr=self.head
        print("None-->",end="")
        while itr is not None:
            print((itr.data),end="-->")
            itr=itr.next
        print("None")
    def reverseprint(self):
        itr=self.tail
        print("None-->",end="")
        while itr is not None:
            print(itr.data,end="-->")
            itr=itr.prev
        print("None")
    def delete_first(self):
        itr=self.head
        self.head=self.head.next
        self.head.prev=None
    def delete_last(self):
        itr=self.tail
        self.tail=self.tail.prev
        self.tail.next=None


ll=DoublyLinkedList()
ll.insert_at_first(10)
ll.insert_at_last(20)
ll.insert_at_first(5)
ll.printll()
ll.reverseprint()
ll.delete_first()
ll.printll()
ll.delete_last()
ll.printll()
        