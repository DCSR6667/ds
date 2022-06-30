'''
This problem can be solved by binary search pattern--O(logn)
the intution behind it is we will solve this problem by bottom--up approach
it is reverse way of binary search(top--down)
'''


def position(nums,target):
    start=0
    end=1
    if target>nums[end]:
        temp=end+1
        end=end+(end-start+1)*2
        start=temp
    return binarysearch(nums,target,start,end)
def binarysearch(nums,target,low,high):
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low+=1
            else:
                high-=1
        return -1
nums=[1,2,3,4,5]
target=5
print(position(nums,target))