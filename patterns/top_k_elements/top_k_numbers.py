'''1..this problem can be solved by using heap
 
   heapify method---O(nlogk+klogn)----space--O(n)
          (or)
     (largest element--use min heap-----time--O(nlogk)--space--O(k)
     smallest element--use max heap
       and we will restrict the size of heap  to k so that 
        insert--O(logk) and delete--O(logk)
        and the size of heap will be--O(k))'''

import heapq
def top_k_num(nums,k):
    res=[]
    maxheap=[i*-1 for i in nums]
    heapq.heapify(maxheap)
    for i in range(k):
        res.append(-1*(heapq.heappop(maxheap)))
    return res

def top_k_num1(nums,k):
    minheap=[]
    for i in nums:
        if len(minheap)<k:
            heapq.heappush(minheap,i)
        elif i>minheap[0]:
            heapq.heappop(minheap)
            heapq.heappush(minheap,i)
    return minheap








