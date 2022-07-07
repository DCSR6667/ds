def binary_search(arr,target,s,e):
    mid=s+(e-s)//2
    if s>e:
        return -1
    if arr[mid]==target:
        return mid
    if arr[mid]>target:
        return binary_search(arr,target,s,mid-1)
    else:
        return binary_search(arr,target,mid+1,e)
print(binary_search([1,2,3,4,5],10,0,4))