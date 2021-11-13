class Node:
    def __init__(self,value=None):
        self.left=None
        self.value=value
        self.right=None
        self.height=0
def preorder(p):
    if p is not None:
        print(p.value,end="-->")
        preorder(p.left)
        preorder(p.right)

def nodeheight(p):
    hl=p.left.height if (p is not None and p.left is not None) else 0
    hr=p.right.height if (p is not None and p.right is not None) else 0
    if hl>hr:
        return hl+1
    else:
        return hr+1

def balancefactor(p):
   hl=p.left.height+1 if (p is not None and p.left is not None) else 0
   hr=p.right.height+1 if (p is not None and p.right is not None) else 0
   
   return hl-hr

def llrotation(p):
    pl=p.left
    plr=pl.right
    pl.right=p
    p.left=plr
    p.height=nodeheight(p)
    pl.height=nodeheight(pl)
    '''if root is p:
        root=pl'''
    
    
    return pl

def lrrotation(p):
    pl=p.left
    plr=pl.right

    pl.right=plr.left
    p.left=plr.right
    plr.left=pl
    plr.right=p
    '''if root is p:
        root=plr'''
    
   
   
    return plr
def rrrotation(p):
    pr=p.right
    prl=pr.left

    p.right=prl
    pr.left=p
    p.height=nodeheight(p)
    pr.height=nodeheight(pr)
    '''if root is p:
        root=pr'''
    return pr

def rlrotation(p):
    pr=p.right
    prl=pr.left

    p.right=prl.left
    pr.left=prl.right
    prl.left=p
    prl.right=pr
    '''if root is p:
        root=prl'''
    return prl

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




def insert(p,key):
    if p is None:
        n=Node(key)
        return n
    if key<p.value:
        p.left=insert(p.left,key)
    elif key>p.value:
        p.right=insert(p.right,key)
    p.height=nodeheight(p)
    
    if balancefactor(p)==2 and balancefactor(p.left)==1:
        return llrotation(p)
    elif balancefactor(p)==2 and balancefactor(p.left)==-1:
        return lrrotation(p)
    elif balancefactor(p)==-2 and balancefactor(p.right)==-1:
        return rrrotation(p)
    elif balancefactor(p)==-2 and balancefactor(p.right)==1:
        return rlrotation(p)
    return p



def delete(p,key):
    if p is None:
        return p
    if key>p.value:
        p.right=delete(p.right,key)
    elif key<p.value:
        p.left=delete(p.left,key)
    elif key==p.value:
        if p.left is None and p.right is None:
            '''if root is p:
                root=None'''
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
    p.height=nodeheight(p)
   
   

    if balancefactor(p)==2 and balancefactor(p.left)==1:
        return llrotation(p)
    elif balancefactor(p)==2 and balancefactor(p.left)==-1:
        return lrrotation(p)
    elif balancefactor(p)==2 and balancefactor(p.left)==0:
        return llrotation(p)
    elif balancefactor(p)==-2 and balancefactor(p.right)==-1:
        return rrrotation(p)
    elif balancefactor(p)==-2 and balancefactor(p.right)==1:
        return rlrotation(p)
    elif balancefactor(p)==-2 and balancefactor(p.right)==0:
        return rrrotation(p)
    return p
    
    
    
    
root=insert(None,30)
root=insert(root,10)
root=insert(root,40)
root=insert(root,5)
root=insert(root,20)
root=delete(root,40)




preorder(root)
