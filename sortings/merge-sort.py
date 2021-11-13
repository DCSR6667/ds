
def mergesort(nums,l,h):
    if l<h:
        mid=(l+h)//2
        mergesort(nums,l,mid)
        mergesort(nums,mid+1,h)
        merge(nums,l,mid,h)
def merge(nums,l,mid,h):
    i,j,k=l,mid+1,l
    b=[None for x in range(h+1)]
    while i<=mid and j<=h:
        if nums[i]<nums[j]:
            b[k]=nums[i]
            k,i=k+1,i+1
        else:
            b[k]=nums[j]
            k,j=k+1,j+1
    while i<=mid:
        b[k]=nums[i]
        k,i=k+1,i+1

    while j<=h:
        b[k]=nums[j]
        k,j=k+1,j+1
    i=l
    while i<=h:
        nums[i]=b[i]
        i+=1

nums=[2,9,4,8,1]
mergesort(nums,0,len(nums)-1)
print(nums)
