'''this can be done by subset pattern--(processing/unprocessing)'''
def phone(ans,s):
    if len(s)==0:
        print(ans)
        return
    digit=int(s[0])
    start=(digit-1)*3
    end=digit*3
    for i in range(start,end):
        phone(ans+chr(97+i),s[1:])

def phone1(ans,s):
    if len(s)==0:
        l=[]
        l.append(ans)
        return l
    digit=int(s[0])
    start=(digit-1)*3
    end=digit*3
    lis=[]
    for i in range(start,end):
        lis=lis+phone1(ans+chr(97+i),s[1:])
    return lis

def phone2(ans,s,l):
    if len(s)==0:
        l.append(ans)
        return l
    digit=int(s[0])
    start=(digit-1)*3
    end=digit*3
    for i in range(start,end):
        phone2(ans+chr(97+i),s[1:],l)
    return l

def count(ans,s):
    if len(s)==0:
        return 1
    digit=int(s[0])
    start=(digit-1)*3
    end=digit*3
    c=0
    for i in range(start,end):
        c=c+count(ans+chr(97+i),s[1:])
    return c
print(count("","12"))