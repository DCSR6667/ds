'''1..this can be solved by using heap
     heapify method---O(nlogk+k1logn+(k2-k1)logn)
          (or)
     (largest element--use min heap-----time--O(nlogk+nlogk+n)--space--O(k)
     smallest element--use max heap
       and we will restrict the size of heap  to k so that 
        insert--O(logk) and delete--O(logk)
        and the size of heap will be--O(k))
           '''
import heapq
def sum(arr,k1,k2):
    heapq.heapify(arr)
    i=1
    while i<=k1:
        heapq.heappop(arr)
        i+=1
    i=1
    sum=0
    while i<=(k2-k1-1):
        sum+=(heapq.heappop(arr))
        i+=1
    return sum

def small(arr,k):
    heap=[]
    for i in arr:
        if len(heap)<k:
            heapq.heappush(heap,i*-1)
        elif i<(heap[0])*-1:
            heapq.heappop(heap)
            heapq.heappush(heap,i*-1)
    i=1
    n=len(heap)
    while i<=(n-k+1):
        ele=heapq.heappop(heap)
        i+=1
    return ele


def sum1(arr,k1,k2):
    k1val=-1*small(arr,k1)
    k2val=-1*small(arr,k2)
    sum=0
    for i in arr:
        if i>k1val and i<k2val:
            sum+=i
    return sum

print(sum1([1, 3, 12, 5, 15, 11],3,6))
