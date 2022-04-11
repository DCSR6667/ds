def quicksort(arr,l,r):
    if l<r:
        pos=partition(arr,l,r)
        quicksort(arr,l,pos-1)
        quicksort(arr,pos+1,r)

def partition(arr,l,r):
    pivot=arr[l]
    i=l+1
    j=r
    while i<j:
        while i<r and arr[i]<=pivot:
            i+=1
        while j>l and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[l]=arr[l],arr[j]
    return j


arr=[3,5,8,1,2]
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)
