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
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        elif loc==0:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
        elif loc==self.length():
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            temp1=temp.next
            newnode.prev=temp
            newnode.next=temp1
            temp.next=newnode
            temp1.prev=newnode
           
           
    
    def display(self):
        temp=self.head
        if temp is None:
            print("DLinkedList is empty")
        else:
            while temp:
                print(temp.value,end="-->")
                temp=temp.next

    def length(self):
        temp=self.head
        count=0
        if temp is None:
            return 0
        else:
            while temp:
                count+=1
                temp=temp.next
            return count

    
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
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            temp1=temp.next.next
            if temp.next is self.tail:
                self.tail=temp
            temp.next=temp1
            if temp1:
                temp1.prev=temp
            
         
         
            



















        
    