def selectionsort(nums,n):
    i=0
    while i<n-1:
        k,j=i,i+1
        while j<n:
            if nums[j]<nums[k]:
                k=j
            j+=1
        temp=nums[i]
        nums[i]=nums[k]
        nums[k]=temp
        i+=1
nums=[3,1,8,5,4]
selectionsort(nums,5)
print(nums)
