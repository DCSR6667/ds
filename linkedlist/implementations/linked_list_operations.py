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
        elif loc==self.length():
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

    def length(self):
        if self.head is None:
            return 0
        else:
            temp=self.head
            count=0
            while temp:
                count+=1
                temp=temp.next
            return count
    
    
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
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            temp1=temp.next
            if temp1 is self.tail:
                self.tail=temp
            temp.next=temp1.next
            temp1.next=None
           
        
      
      









