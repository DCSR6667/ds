'''
factors1 can be done in O(n)
factors2 can be done in O(sqrt(n))'''
def factors1(num):
    i=1
    l=[]
    while i<=num:
        if num%i==0:
            l.append(i)
        i+=1
    return l

def factors2(num):
    i=1
    l=[]
    while i*i<=num:
        if num%i==0:
            if (num//i)==i:
                l.append(i)
            else:
                l.append(i)
                l.append(num//i)

        i+=1
    return l

print(factors2(20))
