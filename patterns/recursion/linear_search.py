def find(arr,target,i):
    if i==len(arr):
        return -1
    if arr[i]==target:
        return i
    return find(arr,target,i+1)

def findlastindex(arr,target,i):
    if i==-1:
        return -1
    if arr[i]==target:
        return i
    return findlastindex(arr,target,i-1)
# l is in argument
def findallindex(arr,target,l,i):
    if i==len(arr):
        return l
    if arr[i]==target:
        l.append(i)
    return findallindex(arr,target,l,i+1)
# l is in body
def findallindex2(arr,target,i):
    l=[]
    if i==len(arr):
        return l
    if arr[i]==target:
        l.append(i)
    lis=findallindex2(arr,target,i+1)
    l=l+lis
    return l
    
arr=[1,2,3,4,9,9,9,8]
print(findallindex2(arr,9,0))