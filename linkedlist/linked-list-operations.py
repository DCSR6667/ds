class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    
    def insert(self,val,loc):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        elif loc==0:
            newnode.next=self.head
            self.head=newnode
        elif loc==1:
            self.tail.next=newnode
            self.tail=newnode
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            newnode.next=temp.next
            temp.next=newnode
            if temp is self.tail:
                self.tail=newnode
        return "inserted successfully"
    
    
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
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
            print("linked list is empty we cant perform delete operation")
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
                temp=self.head
                while temp.next is not self.tail:
                    temp=temp.next
                self.tail=temp
                temp.next=None
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





    


















