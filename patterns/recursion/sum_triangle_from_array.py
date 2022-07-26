'''this can be solved by using recursion'''
def sum(arr):
    if len(arr)==1:
        return arr
    temp=[0]*(len(arr)-1)
    for i in range(0,len(arr)-1):
        temp[i]=arr[i]+arr[i+1]
    return sum(temp)
#with out loop
def sum1(arr):
    if len(arr)==1:
        return arr
    temp=adj(arr,0,[])
    return sum1(temp)
def adj(arr,i,l):
    if i>=len(arr)-1:
        return l
    l.append((arr[i]+arr[i+1]))
    return adj(arr,i+1,l)

print(sum1([1,2,3,4,5]))