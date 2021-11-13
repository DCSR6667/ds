class Node:
    def __init__(self,value=None):
        self.left=None
        self.value=value
        self.right=None


def insert(p,key):
    if p is None:
        n=Node(key)
        return n
    if key<p.value:
        p.left=insert(p.left,key)
    elif key>p.value:
        p.right=insert(p.right,key)
    return p

def inserti(p,key):
    r=None
    while p is not None:
        r=p
        if key==p.value:
            return
        elif key>p.value:
            p=p.right
        else:
            p=p.left
    n=Node(key)
    if r is not None:
        if n.value>r.value:
            r.right=n
        else:
            r.left=n
    else:
        return n



def search(p,key):
    if p is None:
        return None
    if key==p.value:
        return p
    elif key>p.value:
        return search(p.right,key)
    else:
        return search(p.left,key)

def searchi(p,key):
    while p is not None:
        if key==p.value:
            return p
        elif key>p.value:
            p=p.right
        else:
            p=p.left
    return None


    
def preorder(root):
    if root is not None:
        print(root.value,end="-->")
        preorder(root.left)
        preorder(root.right)

def height(p):
    if p is not None:
        if height(p.left)>height(p.right):
            return height(p.left)+1
        else:
            return height(p.right)+1
    else:
        return 0

def inorderp(p):
    while p is not None and p.right is not None:
        p=p.right
    return p

def inorders(p):
    while p is not None and p.left is not None:
        p=p.left
    return p



root=inserti(None,10)
inserti(root,20)
inserti(root,9)
inserti(root,11)
inserti(root,2)
if searchi(root,100) is not None:
    print("true")
else:
    print("false")
preorder(root)

def delete(p,key):
    if p is None:
        return p
    if key>p.value:
        p.right=delete(p.right,key)
    elif key<p.value:
        p.left=delete(p.left,key)
    elif key==p.value:
        if p.left is None and p.right is None:
            if root is p:
                root=None
            
            
            return None
        else:
            if height(p.left)>height(p.right):
                q=inorderp(p.left)
                p.value=q.value
                p.left=delete(p.left,q.value)
            else:
                q=inorders(p.right)
                p.value=q.value
                p.right=delete(p.right,q.value)
    return p

delete(root,10)
print()
preorder(root)
delete(root,20)
print()
preorder(root)




