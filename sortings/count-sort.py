import math
def countsort(nums):
    b=[0 for i in range(max(nums)+1)]
    for i in nums:
        b[i]+=1
    i,j=0,0
    while i<len(b): 
        if b[i]>0:
            nums[j]=i
            j+=1
            b[i]-=1
        else:
            i+=1


def max(nums):
    max=-math.inf
    for i in nums:
        if i>max:
            max=i
    return max

nums=[4,9,5,7,1]
countsort(nums)
print(nums)