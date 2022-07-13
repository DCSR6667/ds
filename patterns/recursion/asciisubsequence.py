'''this can be done by subset pattern--(processing/unprocessing)'''
def asciiseq(ans,s):
    if len(s)==0:
        l=[]
        l.append(ans)
        return l
    a=asciiseq(ans+s[0],s[1:])
    b=asciiseq(ans,s[1:])
    c=asciiseq(ans+str(ord(s[0])),s[1:])
    return a+b+c

print(asciiseq("","ab"))
