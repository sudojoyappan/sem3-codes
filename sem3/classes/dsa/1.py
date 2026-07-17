class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def insert_at_end(self,data):
        node=Node(data)
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        itr.next=node
    def printall(self):
        itr=self.head
        while itr is not None:
            print(itr.data,end="")
            print("-->",end="")
            itr=itr.next
        print("None")
    def print_second_last(self):
        itr=self.head
        while itr.next.next is not None:
            itr=itr.next
        print(itr.data)
    

    def middle(self):
        fastP = self.head
        slowP = self.head
        while fastP.next is not None:
            fastP=fastP.next.next
            slowP=slowP.next
            if fastP is None:
                break
        print(slowP.data)

    def insert_at_k(self,data,k):
        itr=self.head
        count=1
        while count!=k:
            itr=itr.next
            count+=1
        temp=itr.next
        node = Node(data)
        itr.next=node
        node.next=temp

    def append(self , L):
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        itr.next=L.head

    def print_kth_last(self,data,k):
        fastP=self.head
        slowP=self.head
        count=1
        while fastP.next is not None:
            count+=1
            fastP=fastP.next
            if count>k:
                slowP=slowP.next
        print(slowP.data)
        