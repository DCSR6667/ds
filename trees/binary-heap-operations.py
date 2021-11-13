def insertmax(l,n):
    temp=l[n]
    i=n
    while i>1 and temp>l[i//2]:
        l[i]=l[i//2]
        i=i//2
    l[i]=temp

def deletemax(l,n):
    x=l[1]
    l[1]=l[n]
    l[n]=x
    i=1
    j=2*i
    while j<n-1:
        if l[j+1]>l[j]:
            j=j+1
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
            i=j
            j=2*j
        else:
            break

def insertmin(l,n):
    temp=l[n]
    i=n
    while i>1 and temp<l[i//2]:
        l[i]=l[i//2]
        i=i//2
    l[i]=temp

def deletemin(l,n):
    x=l[1]
    l[1]=l[n]
    l[n]=x
    i=1
    j=2*i
    while j<n-1:
        if l[j+1]<l[j]:
            j=j+1
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
            i=j
            j=2*j
        else:
            break



l=[0,2,1,6,4,7]
i=2
while i<=5:
    insertmin(l,i)
    i=i+1
i=1
while i<=5:
    print(l[i],end="-->")
    i=i+1
print()
i=5
while i>1:
    deletemin(l,i)
    i=i-1
i=1

while i<=5:
    print(l[i],end="-->")
    i=i+1





