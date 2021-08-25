class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
class stack:
    def __init__(self):
        self.l=LinkedList()
    
    def isempty(self):
        if self.l.head is None:
            return True
        else:
            return False

    def push(self,value):
        node=Node(value)
        node.next=self.l.head
        self.l.head=node
    
    def pop(self):
        if self.isempty():
            print("stack is empty we cant delete element")
        else:
            self.l.head=self.l.head.next

    def peek(self):
        if self.isempty():
            print("stack is empty we cant get top element")
        else:
            return self.l.head.value
    
    def __str__(self):
        temp=self.l.head
        s=""
        while temp:
            s=s+str(temp.value)+"-->"
            temp=temp.next
        return s

    def deletestack(self):
        self.l.head=None

