'''In the first approach creation of heap takes O(nlogn)  but we can reduce
 to O(nlogk)---dont know

 In the second approach creation of heap takes O(nlogk)
 '''

## time--O(logn)
def insert(arr,i):
    temp=arr[i]
    while i>0 and temp>arr[(i-1)//2]:
        arr[i]=arr[(i-1)//2]
        i=(i-1)//2
    arr[i]=temp

## time--O(logn)
def delete(arr,heapsize):
    x=arr[0]
    arr[0]=arr[heapsize]
    i=0
    j=(2*i)+1
    while j<heapsize-1:
        if arr[j+1]>arr[j]:
            j=j+1
        if arr[j]>arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
            i=j
            j=(2*j)+1
        else:
            break
    arr[heapsize]=x
    return arr[heapsize]

## time--O(nlogn)
def createheap(arr):
    for i in range(1,len(arr)):
        insert(arr,i)

## time--O(2nlogn)
def heapsort(arr):
    createheap(arr)
    for i in range((len(arr)-1),0,-1):
        delete(arr,i)
arr=[10,20,30,25,5,40,35]
createheap(arr)
print(arr)


#--------------------------------------------------------------------------
'''Heap implementation using heapq library
   by default it is min heap 
   we can implement max heap simply by multiplicating the numbers with negative sign '''



# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap and adjust the heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element and adjsut heap
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))

# using heappushpop() to push and pop items simultaneously
# pops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li, 2))
  
# using heapreplace() to push and pop items simultaneously
# pops 3
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li, 2))

