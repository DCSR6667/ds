def prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)

if prime(11):
    print("it is a prime number")
else:
    print("it is not a prime number")