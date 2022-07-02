'''
this problem can be solved by binary search pattern---O(logn)'''

def sqrt(num,p):
    l,h=0,num
    root=0
    while l<=h:
        mid=l+(h-l)//2
        if mid*mid==num:
            return mid
        elif mid*mid>num:
            h=mid-1
        else:
            l=mid+1
            root=mid
    inc=0.1
    i=0
    while i<p:
        while root*root<num:
            root+=inc
        root-=inc
        inc/=10
        i+=1
    return root

print(sqrt(40,5))
