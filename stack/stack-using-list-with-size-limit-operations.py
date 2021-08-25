class stack:
    def __init__(self,size):
        self.l=[]
        self.size=size

    def __str__(self):
        if self.l is None:
            return "stack is empty"
        else:
            return str(self.l[::-1])
    
    def isempty(self):
        if self.l==[]:
            return True
        else:
            return False
    
    def isfull(self):
        if len(self.l)==self.size:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isfull():
            print("stack is full we cant insert element")
        else:
            self.l.append(value)

    def pop(self):
        if self.isempty():
            print("stack is empty we cant delete element")
        else:
            self.l.pop()
    
    def peek(self):
        if self.isempty():
            print("stack is empty we cant get element")
        else:
            return self.l[len(self.l)-1]

    def deletestack(self):
        self.l=None




    