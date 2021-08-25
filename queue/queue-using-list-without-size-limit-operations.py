class queue:
    def __init__(self):
        self.l=[]

    def isempty(self):
        if self.l==[]:
            return True
        else:
            return False

    def enqueue(self,value):
        self.l.append(value)

    def dequeue(self):
        if self.isempty():
            print("we cant delete element queue is empty")
        else:
            self.l.pop(0)
    
    def peek(self):
        if self.isempty():
            print("we cant get element  because queue is empty")
        else:
            return self.l[0]
    
    def __str__(self):
        l1=[str(i) for i in self.l]
        return ' '.join(l1)'


    

    
