def sorted(arr,i):
    if i==len(arr)-1:
        return True
    return arr[i]<arr[i+1] and sorted(arr,i+1)

print(sorted([1,2,3,6,5],0))