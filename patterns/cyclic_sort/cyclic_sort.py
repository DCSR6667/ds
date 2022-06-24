'''if element is in correct index then increment i and 
   and if element is not in correct index then swap the element to its correct index
   generally this will take o(n2) time complexity.but whenever you will given array with elements 
   in the range upto N then this will take O(n) time complexity
'''

def cyclic_sort(nums):
    i=0
    while i<len(nums):
        pos=nums[i]-1
        if i!=pos:
            nums[i],nums[pos]=nums[pos],nums[i]
        else:
            i+=1

    

nums=[2,4,5,1,3]
cyclic_sort(nums)
print(nums)
