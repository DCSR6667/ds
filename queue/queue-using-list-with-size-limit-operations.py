class queue:
    def __init__(self,size):
        self.l=[None]*size
        self.f=-1
        self.r=-1
        self.size=size
    
    def isempty(self):
        if self.f==-1:
            return True
        else:
            return False
    
    def isfull(self):
        if self.r==self.size-1:
            return True
        else:
             return False

    def enqueue(self,value):
        if self.isfull():
            print("queue is full we cant insert element")
        elif self.f==-1 and self.r==-1:
            self.f,self.r=0,0
            self.l[self.r]=value
        else:
            self.r=self.r+1
            self.l[self.r]=value
    
    def dequeue(self):
        if self.isempty():
            print("we cant delete element  queue is empty")
        elif self.f==self.r:
            self.f,self.r=-1,-1
        else:
            self.f+=1
    
    def peek(self):
        if self.isempty():
            print("we cant get element because queue is empty")
        else:
            return self.l[self.f]
    
    def display(self):
        if self.f==-1:
            print("queue is empty")
        else:
            i=self.f
            while i<=self.r:
                print(self.l[i],end=" ")
                i+=1

#circular queue
class cqueue:
     def __init__(self,size):
        self.l=[None]*size
        self.f=-1
        self.r=-1
        self.size=size
        
     def isempty(self):
        if self.f==-1:
            return True
        else:
            return False

     def isfull(self):
         if self.f==0 and self.r==self.size-1:
             return True
         elif self.r==self.f-1:
             return True
         else:
             return False
     def enqueue(self,value):
         if self.isfull():
             print("queue is full we cant insert element")
         elif self.f==-1:
             self.f,self.r=0,0
             self.l[self.r]=value
         elif self.r==self.size-1 and self.f!=0:
             self.r=0
             self.l[self.r]=value
         else:
             self.r+=1
             self.l[self.r]=value

     def peek(self):
        if self.isempty():
            print("we cant get element because queue is empty")
        else:
            return self.l[self.f]
    
     def dequeue(self):
         if self.isempty():
             print("we cant delete element queue is empty")
         elif self.f==self.r:
             self.f=-1
             self.r=-1
         elif self.f==self.size-1 and self.r<self.f:
             self.f=0
         else:
             self.f+=1
    
     def display(self):
         i=self.f
         while i!=self.size:
             print(self.l[i],end=" ")
             i=i+1
         i=i-1
         if i!=self.r:
             i=0
             while i<=self.r:
                 print(self.l[i],end=" ")
                 i=i+1
        
cq=cqueue(4)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.dequeue()
cq.dequeue()
cq.enqueue(5)
cq.enqueue(6)
print(cq.peek())
cq.display()

    
    
    


        
        






