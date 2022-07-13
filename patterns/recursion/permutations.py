'''this can be done by subset pattern--(processing/unprocessing)'''
def permutation(ans,s):
    if len(s)==0:
        print(ans)
        return
    size=len(ans)+1
    ch=s[0]
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        permutation(first+ch+last,s[1:])


def permutation1(ans,s):
    if len(s)==0:
        l=[]
        l.append(ans)
        return l
    size=len(ans)+1
    ch=s[0]
    lis=[]
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        lis=lis+permutation1(first+ch+last,s[1:])
    return lis

def permutation2(ans,s,l):
    if len(s)==0:
        l.append(ans)
        return l
    size=len(ans)+1
    ch=s[0]
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        permutation2(first+ch+last,s[1:],l)
    return l
print(permutation2("","abc",[]))


