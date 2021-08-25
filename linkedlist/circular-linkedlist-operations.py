class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class CLinkedList:
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
            self.tail.next=node
            self.head=node
        elif loc==1:
            node.next=self.head
            self.tail.next=node
            self.tail=node
        else:
            i=1
            temp=self.head
            while i<loc:
                temp=temp.next
                i=i+1
            node.next=temp.next
            temp.next=node
            if temp is self.tail:
                self.tail=node
                self.tail.next=self.head
   
   
    def display(self):
        if self.head is None:
            print("CLinkedList is empty")
        else:
            temp=self.head
            while temp.next is not self.tail:
                print(temp.value,end="-->")
                temp=temp.next
            print(temp.value,end="-->")
            temp=temp.next
            if temp:
                print(temp.value)
    

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
        elif loc==1:
             if self.head is self.tail:
                self.head=None
                self.tail=None
             else:
                temp=self.head
                while temp.next is not self.tail:
                    temp=temp.next
                self.tail=temp
                self.tail.next=self.head
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
                self.tail.next=self.head
            temp.next=temp.next.next

            


    








            


