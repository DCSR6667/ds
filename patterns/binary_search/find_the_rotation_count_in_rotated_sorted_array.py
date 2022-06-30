'''this can be done by binary search pattern--O(logn)
pivot is nothing but largest element in rotated sorted array
rotation count is nothing but pivot+1

'''
def pivot(nums):
    start,end=0,len(nums)-1
    while start<=end:
        mid=start+(end-start)//2
        if mid<end and nums[mid]>nums[mid+1]:
            return mid
        if mid>start and nums[mid]<nums[mid-1]:
            return mid-1
        if nums[start]>=nums[mid]:
            end=mid-1
        else:
            start=mid+1
    return -1

def rotation_count(nums):
    p=pivot(nums)
    return p+1
print(rotation_count([5,6,7,1,2,3]))