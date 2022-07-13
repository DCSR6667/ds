'''this problem can be solved by subset pattern'''
def print1(ans,c,r):
    if c==1 and r==1:
        print(ans)
    if r>1 and c>1:
        print1(ans+"D",r-1,c-1)
    if r>1:
        print1(ans+"V",r-1,c)
    if c>1:
        print1(ans+"H",r,c-1)

def print2(ans,c,r):
    if c==1 and r==1:
        l=[]
        l.append(ans)
        return l
    lis=[]
    if r>1 and c>1:
        lis=lis+print2(ans+"D",r-1,c-1)
    if r>1:
        lis=lis+print2(ans+"V",r-1,c)
    if c>1:
        lis=lis+print2(ans+"H",r,c-1)
    return lis

print(print2("",3,3))