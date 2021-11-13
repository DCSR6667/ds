class Node:
    def __init__(self,value=None):
        self.prev=None
        self.value=value
        self.next=None
class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,val,loc):
        node=Node(val)
        if self.head is None:
            self.head=node
            self.tail=node
        elif loc==0:
            node.next=self.head
            self.head.prev=node
            self.head=node
        elif loc==1:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            node.next=temp.next
            if temp.next:
                temp.next.prev=node
            temp.next=node
            node.prev=temp
            if temp is self.tail:
                self.tail=node
    
    def display(self):
        temp=self.head
        if temp is None:
            print("DLinkedList is empty")
        else:
            while temp:
                print(temp.value,end="-->")
                temp=temp.next
    
    def search(self,data):
        temp=self.head
        while temp:
            if temp.value==data:
                return True
            temp=temp.next
        return False
    
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def delete(self,loc):
        if self.isempty():
            print("we cant delete element because DLinkedList is empty")
        elif loc==0:
            if self.head is self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
        elif loc==1:
            if self.head is self.tail:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=None
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            if temp is self.tail:
                print("we cant delete ele")
                return
            if temp.next is self.tail:
                self.tail=temp
            temp.next=temp.next.next
            if temp.next:
                temp.next.prev=temp
            

















        
    