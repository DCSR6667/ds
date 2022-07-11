'''this can be solved by subset pattern (taking or not taking)'''
def iterative_subseq(arr):
    outer=[[]]
    for num in arr:
        i=0
        size=len(outer)
        while i<size:
            print('hi')
            l=outer[i].copy()
            l.append(num)
            outer.append(l)
            i+=1
    print(outer)

iterative_subseq([1,2,3])

