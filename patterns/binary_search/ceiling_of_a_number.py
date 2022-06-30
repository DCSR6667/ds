'''
this can be solved by binary search pattern--O(logn)
ceiling of a number is like smallest number that should be >=target
'''
def ceiling_of_a_number(arr,key):
  # TODO: Write your code here
    start = 0
    end = len(arr) -1
    if target>arr[end]:
        return -1

    while start <= end:
        index = start+(end-start)//2
        if arr[index]==key:
            return index
        
        if arr[index] < key:
    
            start = index + 1
        elif arr[index] > key:
            end = index - 1
          
          
    return start
arr=[1,2,5,6]
key=4
print(ceiling_of_a_number(arr,key))