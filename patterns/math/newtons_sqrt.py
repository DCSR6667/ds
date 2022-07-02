'''it depends on formula--O(logn)f(n)
    root=0.5*(x+(num//x))
     x=predicted root
     root=actual root 
     err=|root-x|'''
import math
def newtonsqrt(num):
    x=num
    root=0
    while True:
        root=0.5*(x+(num//x))
        err=math.fabs(root-x)
        if err<1:
            break
        x=root
    return root

print(newtonsqrt(9))

