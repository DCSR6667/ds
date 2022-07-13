'''this problem can be solved by subset pattern'''
def print1(ans,c,r):
    if c==1 and r==1:
        print(ans)
    if r>1:
        print1(ans+"D",r-1,c)
    if c>1:
        print1(ans+"R",r,c-1)

print1("",3,3)