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
        node=Node(val)
        if self.head is None:
            self.head=node
            self.tail=node
        elif loc==0:
            node.next=self.head
            self.head.prev=node
            self.head=node
            self.head.prev=self.tail
            self.tail.next=self.head
        elif loc==1:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.tail.next=self.head
            self.head.prev=self.tail
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
                self.tail.next=self.head
                self.head.prev=self.tail
    
    def display(self):
        if self.head is None:
            print("CDlinked is empty")
        else:
            temp=self.head
            while temp.next is not self.tail:
                print(temp.value,end="-->")
                temp=temp.next
            print(temp.value,end="-->")
            if temp.next:
                print(temp.next.value)
    
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
            if temp.next:
                if temp.next.value==data:
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
        elif loc==1:
            if self.head is self.tail:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=self.head
                self.head.prev=self.tail
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
            temp.next.prev=temp
            
    


cd=CDLinkedList()
cd.insert(0,1)
cd.insert(1,1)
cd.insert(2,1)
cd.insert(3,1)
cd.insert(4,1)

cd.display()
print()

cd.delete(3)
cd.delete(3)
cd.insert(1,1)
cd.delete(4)



cd.display()


            




