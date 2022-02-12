def move(l):
    i,j=0,len(l)-1
    while i<j:
        if l[i]<0:
            i=i+1
        elif l[i]>0 and l[j]<0:
            l[i],l[j]=l[j],l[i]
            i,j=i+1,j-1
        else:
            j-=1
    return l
print(move([10,6,2,-7,9]))