def insert(a,n):
    temp=a[n]
    i=n
    while i>1 and temp>a[i//2]:
        a[i]=a[i//2]
        i=i//2
    a[i]=temp


def delete(a,n):
    temp=a[1]
    a[1]=a[n]
    a[n]=temp
    i=1
    j=2*i
    while j<n-1:
        if a[j+1]>a[j]:
            j=j+1
        if a[j]>a[i]:
            a[j],a[i]=a[i],a[j]
            i=j
            j=2*j
        else:
            break


l=[0,2,5,1,8,5,7,3]
for i in range(2,len(l)):
    insert(l,i)
i=7
while i>1:
    delete(l,i)
    i-=1
for ele in l:
    print(ele,end=" ")
