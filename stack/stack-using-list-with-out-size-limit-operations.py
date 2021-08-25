class stack:
    
    def __init__(self):
        self.l=[]

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
    
    def push(self,value):
        self.l.append(value)

    def pop(self):
        if self.isempty():
            print("stack is empty we cant delete element")
        else:
            self.l.pop()
    
    def peek(self):
        if self.isempty():
            print("stack is empty we cant get top element")
        else:
            return self.l[len(self.l)-1]
        
    def deletestack(self):
        self.l=None



   
   