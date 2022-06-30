n=6
res=0
power=5
while n>0:
    last=(n & 1)
    res=res+(last*power)
    power=power*5
    n=n>>1
   
print(res)