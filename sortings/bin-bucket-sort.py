import math
def max(nums):
    max=-math.inf
    for i in nums:
        if i>max:
            max=i
    return max

def binsort(nums):
    b=[[] for i in range(max(nums)+1)]
    for i in nums:
        b[i].append(i)
    i,j=0,0
    while i<len(b):
        if b[i]==[]:
            i=i+1
        else:
            nums[j]=b[i].pop()
            j=j+1


nums=[7,3,8,3,5,7,9,5]
binsort(nums)
print(nums)
