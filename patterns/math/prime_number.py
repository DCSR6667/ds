'''it will take time complexity--O(squareroot(n))'''

def isprime(n):
    i=2
    if n<=1:
        return False
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

nums=[1,2,3,4,5,6,7,8]
for i in nums:
    print(i,isprime(i))