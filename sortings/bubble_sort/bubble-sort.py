def bubblesort(nums,n):
    i=0
    while i<n-1:
        j=0
        flag=0
        while j<n-1-i:
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=1
            j+=1
        if flag==0:
            break
        i+=1
nums=[3,1,6,2,7]
bubblesort(nums,5)
print(nums)
            