'''this can be done by subset pattern--(processing/unprocessing)'''
def subseq(ans,s):
    if len(s)==0:
        print(ans)
        return
    #add it
    subseq(ans+s[0],s[1:])
    subseq(ans,s[1:])

def subseqret(ans,s):
    if len(s)==0:
        l=[]
        l.append(ans)
        return l
    l=subseqret(ans+s[0],s[1:])
    r=subseqret(ans,s[1:])
    return l+r

def subseqret2(ans,s,l):
    if len(s)==0:
        l.append(ans)
        return l
    subseqret2(ans+s[0],s[1:],l)
    subseqret2(ans,s[1:],l)
    return l
    
    
    
print(subseqret2("","abc",[]))