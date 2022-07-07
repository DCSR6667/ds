def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
def funrev(n):
    if n==0:
        return
    funrev(n-1)
    print(n)
def funboth(n):
    if n==0:
        return
    print(n)
    funboth(n-1)
    print(n)



