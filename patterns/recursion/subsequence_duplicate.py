'''this can be done by subset pattern--(processing/unprocessing)
    but whenever duplicate number exists then add it to the 
    previous added elements in nested list '''
def iterative_subseq(arr):
    outer=[[]]
    arr.sort()
    for i in range(len(arr)):
        start=0
        if i>0 and arr[i]==arr[i-1]:
            start=end+1
        end=len(outer)-1
        j=start
        size=len(outer)
        while j<size:
            l=outer[j].copy()
            l.append(arr[i])
            outer.append(l)
            j+=1
    print(outer)

iterative_subseq([1,2,2,3])

