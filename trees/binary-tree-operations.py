from binarytree import build,tree

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
            return None
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

def createbt():
    val=int(input("enter root value"))
    root=Node(val)
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        p=q.dequeue()
        val=int(input(f" enter left child of {p.value}"))
        if val!=-1:
            temp=Node(val)
            p.left=temp
            q.enqueue(temp)
        val=int(input(f" enter right child of {p.value}"))
        if val!=-1:
            temp=Node(val)
            p.right=temp
            q.enqueue(temp)
    return root

def search(root,data):
    if root is None:
        return False
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        p=q.dequeue()
        if p.value==data:
            return True
        if p.left is not None:
            q.enqueue(p.left)
        if p.right is not None:
            q.enqueue(p.right)
    return False

def insert(root,data):
    if root is None:
        root=Node(data)
        return root
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        p=q.dequeue()
        if p.left is not None:
            q.enqueue(p.left)
        else:
            n=Node(data)
            p.left=n
            return root
            
        if p.right is not None:
            q.enqueue(p.right)
        else:
            n=Node(data)
            p.right=n
            return root
            
    return root

def getdeepestnode(root):
    if root is None:
        return None
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        p=q.dequeue()
        if p.left is not None:
            q.enqueue(p.left)
        if p.right is not None:
            q.enqueue(p.right)
        dnode=p
    return dnode

def deletedeepestnode(root,dnode):
    if root is None:
        return "we cant delete node"
    if root is dnode:
        root=None
        return "success"
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        p=q.dequeue()
        if p.left is not None:
            if p.left is dnode:
                p.left=None
                return "success"
            else:
                q.enqueue(p.left)
        if p.right is not None:
            if p.right is dnode:
                p.right=None
                return "success"
            else:
                q.enqueue(p.right)
    return "failure"

def delete(root,data):
    if root is None:
        return "we cant delete node"
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        root=q.dequeue()
        if root.value==data:
            dnode=getdeepestnode(root)
            root.value=dnode.value
            deletedeepestnode(root,dnode)
            return "success"
        if root.left is not None:
            q.enqueue(root.left)
        if root.right is not None:
            q.enqueue(root.right)
    return "failure"

def deletebinarytree(root):
    if root is not None:
        root=None
    return root
    


    

def preorder(root):
    if root is None:
        return
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)

def preorderiter(root):
    if root is None:
        return None
    p=root
    s=stack()
    while not(s.isempty()) or p!=None:
        if p is not None:
            print(p.value,end=" ")
            s.push(p)
            p=p.left
        else:
            p=s.pop()
            p=p.right


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)

def inorderiter(root):
    if root is None:
        return
    s=stack()
    p=root
    while p!=None or not(s.isempty()):
        if p!=None:
            s.push(p)
            p=p.left
        else:
            p=s.pop()
            print(p.value,end=" ")
            p=p.right

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=" ")

def postorderiter(root):
    if root is None:
        return
    s=stack()
    p=root
    while p!=None or not(s.isempty()):
        if p is not None:
            s.push(p)
            p=p.left
        else:
            if s.peek().right is None:
                p=s.pop()
                print(p.value,end=" ")
                while s.peek() and p==s.peek().right:
                    p=s.pop()
                    print(p.value,end=" ")
            if not(s.isempty()):
                p=s.peek().right
            else:
                p=None

          



def levelorder(root):
    if root is None:
        return None
    q=queue()
    q.enqueue(root)
    while not(q.isempty()):
        p=q.dequeue()
        print(p.value,end=" ")
        if p.left is not None:
            q.enqueue(p.left)
        if p.right is not None:
            q.enqueue(p.right)



def count(root):
    if root is None:
        return 0
    l=count(root.left)
    r=count(root.right)
    return l+r+1

def leafnodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return leafnodes(root.left)+leafnodes(root.right)+1
    else:
        return leafnodes(root.left)+leafnodes(root.right)
    
    

def count2deg(root):
    if root is None:
        return 0
    if root.left and root.right:
        return count2deg(root.left)+count2deg(root.right)+1 
    else:
        return count2deg(root.left)+count2deg(root.right)

def count1deg(root):
    if root is None:
        return 0
    if (root.left and root.right is None) or (root.left is None and root.right):
        return count1deg(root.left)+count1deg(root.right)+1
    else:
        return count1deg(root.left)+count1deg(root.right)


def internalnodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return internalnodes(root.left)+internalnodes(root.right)
    else:
        return internalnodes(root.left)+internalnodes(root.right)+1

def height(root):
    if root is None:
        return -1
    l,r=height(root.left),height(root.right)
    if l>r:
        return l+1
    else:
        return r+1

def level(root):
    if root is None:
        return 0
    l,r=level(root.left),level(root.right)
    if l>r:
        return l+1
    else:
        return r+1
    



root=insert(None,10)
insert(root,20)
insert(root,30)
insert(root,40)
insert(root,50)
insert(root,60)
insert(root,70)
insert(root,80)
print("no of nodes is",count(root))
print("no of leaf nodes is",leafnodes(root))
print("no of internal nodes is",internalnodes(root))

print("no of nodes with degree 1 is",count1deg(root))
print("no of nodes with degree 2 is",count2deg(root))
print("height of binary tree is",height(root))
print("level of binary tree is",level(root))
preorderiter(root)
print()
inorderiter(root)
print()
postorderiter(root)






#----------------------------------------------------------------------------------
# List of nodes
nodes =[3, 6, 8, 2, 11, None, 13]
  
# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
      binary_tree)
  
# Getting list of nodes from
# binarytree
print('\nList from binary tree :', 
      binary_tree.values)

#-----------------------------------------------------------------------------
  
# Create a random binary 
# tree of any height
root = tree()
print("Binary tree of any height :")
print(root)
  
# Create a random binary 
# tree of given height
root2 = tree(height = 2)
print("Binary tree of given height :")
print(root2)
  
# Create a random perfect 
# binary tree of given height
root3 = tree(height = 2,
             is_perfect = True)
print("Perfect binary tree of given height :")
print(root3)


#------------------------------------------------------------------------------------------

            
 
 

       
       





