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
            return self.l.pop()
    
    def peek(self):
        if self.isempty():
            print("stack is empty we cant get top element")
        else:
            return self.l[len(self.l)-1]
        
    def deletestack(self):
        self.l=None

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
            return self.l.pop(0)
    
    def peek(self):
        if self.isempty():
            print("we cant get element  because queue is empty")
        else:
            return self.l[0]
    
    def __str__(self):
        l1=[str(i) for i in self.l]
        return ' '.join(l1)

class Node:
    def __init__(self,value=None):
        self.left=None
        self.value=value
        self.right=None
 
 

def insert(root,value):
    node=Node(value)
    if root is None:
        root=node
        return root
    else:
        q=queue()
        q.enqueue(root)
        while not q.isempty():
            t=q.dequeue()
            
            if t.left is None:
                t.left=node
                return
            else:
                q.enqueue(t.left)
            
            if t.right is None:
                t.right=node
                return
            else:
                q.enqueue(t.right)


def preorder(root):
    if root is not None:
        print(root.value,end="-->")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value,end="-->")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end="-->")

def levelorder(root):
    if root is None:
        print("tree is empty")
    else:
        q=queue()
        print(root.value,end="-->")
        q.enqueue(root)
        while not q.isempty():
            p=q.dequeue()
            if p.left is not None:
                print(p.left.value,end="-->")
                q.enqueue(p.left)
            if p.right is not None:
                print(p.right.value,end="-->")
                q.enqueue(p.right)
            

def count(root):
    if root is None:
        return 0
    else:
        return count(root.left)+count(root.right)+1

def leafnodes(root):
    if root is None:
        return 0
    else:
        if root.left is None and root.right is None:
            return leafnodes(root.left)+leafnodes(root.right)+1
        else:
            return leafnodes(root.left)+leafnodes(root.right) 

def internalnodes(root):
    if root is None:
        return 0
    else:
        if root.left is not None or root.right is not None:
            return internalnodes(root.left)+internalnodes(root.right)+1
        else:
            return internalnodes(root.left)+internalnodes(root.right) 

def degree2nodes(root):
    if root is None:
        return 0
    else:
        if root.left is not None and root.right is not None:
            return degree2nodes(root.left)+degree2nodes(root.right)+1
        else:
            return degree2nodes(root.left)+degree2nodes(root.right) 

def sum(root):
    if root is None:
        return 0
    else:
        return sum(root.left)+sum(root.right)+root.value

def height(root):
    if root is None:
        return 0
    else:
        if height(root.left)>height(root.right):
            return height(root.left)+1
        else:
            return height(root.right)+1
    
def preorderi(root):
    s=stack()
    if root is None:
        print('tree is empty')
    while root is not None or not s.isempty():
        if root is not None:
            print(root.value,end="-->")
            s.push(root)
            root=root.left
        else:
            p=s.pop()
            root=p.right

def inorderi(root):
    s=stack()
    if root is None:
        print("tree is empty")
    else:
        while root is not None or not s.isempty():
            if root is not None:
                s.push(root)
                root=root.left
            else:
                p=s.pop()
                print(p.value,end="-->")
                root=p.right

def postorderi(root):
    s=stack()
    if root is None:
        print("tree is empty")
    else:
        while root is not None or not s.isempty():
            if root is not None:
                s.push(root)
                root=root.left
            else:
                p=s.pop()
                if p>0:
                    s.push(-p )
                    root=p.right
                else:
                    print(p.value,end="-->")
                    root=None
    

        


root=insert(None,10)
insert(root,20)
insert(root,30)
insert(root,40)
insert(root,50)
insert(root,60)
insert(root,70)
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
levelorder(root)
print()
print("count",count(root))
print("leafnodes",leafnodes(root))
print("internalodes",internalnodes(root))
print("degree2nodes",degree2nodes(root))
print("sum",sum(root))
print("height",height(root))
preorderi(root)
print()
inorderi(root)
print()
postorderi(root)





            


    
    
       
       





