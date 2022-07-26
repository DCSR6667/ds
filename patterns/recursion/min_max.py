def min_max(arr,i,min,max):
    if i>=len(arr):
        return min,max
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
    return min_max(arr,i+1,min,max)
l=[1,-2,3,4,10]
print(min_max(l,0,l[0],l[0]))