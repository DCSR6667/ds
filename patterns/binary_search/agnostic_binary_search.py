'''
if we dont know whether the array is sorted either in ascending or descending then that
binary search is called agnostic binary search---O(logn)
'''

def agnostic_binary_search(arr, key):
  # TODO: Write your code here
    asc=arr[0]<arr[-1]
    start = 0
    end = len(arr) -1

    while start <= end:
        index = start+(end-start)//2
        if arr[index]==key:
            return index
        
        if arr[index] < key:
            if asc:
                start = index + 1
            else:
                end = index - 1
        elif arr[index] > key:
            if asc:
                end = index - 1
            else:
                start = index + 1
    return -1
arr=[5,4,3,2,1]
key=2
print(agnostic_binary_search(arr,key))