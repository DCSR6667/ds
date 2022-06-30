def xor(a):
    if a%4==0:
        return a
    if a%4==1:
        return 1
    if a%4==2:
        return a+1
    return 0

a,b=3,9
print(xor(b)^xor(a-1))