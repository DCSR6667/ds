'''
this can be solved by binary search pattern--O(logn)
floor of a number is like greatest number that should be <=target
'''
def floor_of_a_number(arr,key):
  # TODO: Write your code here
    start = 0
    end = len(arr) -1

    while start <= end:
        index = start+(end-start)//2
        if arr[index]==key:
            return index
        
        if arr[index] < key:
    
            start = index + 1
        elif arr[index] > key:
            end = index - 1
          
          
    return end
arr=[1,2,5,6]
key=4
print(floor_of_a_number(arr,key))