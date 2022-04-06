def insertionsort(nums,n):
    i=1
    while i<n:
        j=i-1
        x=nums[i]
        while j>=0 and nums[j]>x:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=x
        i+=1

nums=[3,2,6,5,9]
insertionsort(nums,5)
print(nums)