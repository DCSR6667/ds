import math
def rev(n,digits):
    if n==0:
        return 0
    rem=n%10
    return int(rem*(10**(digits-1)))+rev(n//10,digits-1)

def palindrome(n):
    digits=int(math.log(n)//math.log(10))+1
    return n==rev(n,digits)
print(palindrome(1111))