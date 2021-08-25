class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
class queue:
    def __init__(self):
        self.l=LinkedList()

    def isempty(self):
        if self.l.head is None:
            return True
        else:
            return False

    def enqueue(self,value):
        node=Node(value)
        if self.isempty():
            self.l.head=node
            self.l.tail=node
        else:
            self.l.tail.next=node
            self.l.tail=node
    def dequeue(self):
        if self.isempty():
            print("we cant delete element quueu is empty")
        else:
            if self.l.head is self.l.tail:
                self.l.head=None
                self.l.tail=None
            else:
                self.l.head=self.l.head.next
    
    def peek(self):
        if self.isempty():
            print("we cant get element queue is empty")
        else:
            return self.l.head.value

    def display(self):
        if self.isempty():
            print("we cant delete element quueu is empty")
        else:
            temp=self.l.head
            while temp:
                print(temp.value,end="-->")
                temp=temp.next




        
