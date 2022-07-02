'''
gcd(a,b)=gcd(rem(b,a),a)
lcm(a,b)=a*b//gcd(a,b)
'''

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return a*b//gcd(a,b)
print(gcd(3,9))
print(lcm(3,9))