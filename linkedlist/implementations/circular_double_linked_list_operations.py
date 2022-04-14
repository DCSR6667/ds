class Node:
    def __init__(self,value=None):
        self.prev=None
        self.value=value
        self.next=None
class CDLinkedList:
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
            self.tail.next=newnode
            newnode.prev=self.tail
            self.head=newnode 
        elif loc==self.length():
            newnode.prev=self.tail
            newnode.next=self.head
            self.tail.next=newnode
            self.head.prev=newnode
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
        if self.head is None:
            print("CDlinked is empty")
        else:
            temp=self.head
            while temp is not self.tail:
                print(temp.value,end="-->")
                temp=temp.next
            print(temp.value,end="-->")

    def length(self):
        if self.head is None:
            return 0
        else:
            count=0
            temp=self.head
            while temp is not self.tail:
                count+=1
                temp=temp.next
            count+=1
            return count
           
           
    
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def search(self,data):
        if self.head is None:
            print("CLickedList is empty")
        else:
            temp=self.head
            while temp is not self.tail:
                if temp.value==data:
                    return True
                temp=temp.next
            if temp.value==data:
                return True
        return False 
    
    def delete(self,loc):
        if self.head is None:
            print("we cant delete ele because dcll is empty")
        elif loc==0:
            if self.head is self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.head.prev=self.tail
                self.tail.next=self.head
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            if temp.next is self.tail:
                self.tail=temp
            temp1=temp.next.next
            temp.next=temp1
            temp1.prev=temp
           











            




