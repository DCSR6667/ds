from functools import  reduce
from math import inf
def noofdigits(nums):
    max=-inf
    for i in nums:
        if i>max:
            max=i
    return len(str(max))

def flatten(b):
    return reduce(lambda x,y:x+y,b)


def radixsort(nums):
    digits=noofdigits(nums)
    for digit in range(digits):
        b=[[] for x in range(10)]
        for i in nums:
            index=(i//(10**digit))%10
            b[index].append(i)
        nums=flatten(b)
    return nums

nums=[7,3,8,3,5,7,9,5]
print(radixsort(nums))
    

