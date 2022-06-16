''' this problem can be solved by sliding window pattern---O(n)
calculate sum of window and update max_sum
**but when the length of the window is >3
    update sum
    update l''''

def max_sub_of_size_k(arr,k):
    l,r=0,0
    sum=0
    max_sum=0
    while r<len(arr):
        sum+=arr[r]
       
        if (r-l+1)>k:
            sum-=arr[l]
            l+=1
        max_sum=max(max_sum,sum)
        r+=1
        
    return max_sum
print(max_sub_of_size_k([2, 1, 5, 1, 3, 2],3))



