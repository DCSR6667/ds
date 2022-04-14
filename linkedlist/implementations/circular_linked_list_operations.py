class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class CLinkedList:
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
            self.tail.next=self.head
        elif loc==self.length():
            newnode.next=self.head
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
           
           
   
    def display(self):
        if self.head is None:
            print("CLinkedList is empty")
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
            temp=self.head
            count=0
            while temp is not self.tail:
                count+=1
                temp=temp.next
            count+=1
            return count
            
            
            
    

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
    

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False
    

    def delete(self,loc):
        if self.isempty():
            print("Clinked list is empty we cant delete element")
        elif loc==0:
            if self.head is self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.tail.next=self.head
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
           
            if temp.next is self.tail:
               self.tail=temp
            temp.next=temp.next.next












    








            


