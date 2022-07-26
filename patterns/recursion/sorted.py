def sorted(arr,i):
    if i>=len(arr)-1:
        return True
    if arr[i]>arr[i+1]:
        return False
    return sorted(arr,i+1)

print(sorted([1,2,3,3,5],0))