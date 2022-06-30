power=6
base=3
ans=1
while power>0:
    last=power & 1
    if last==1:
        ans*=base
    base*=base
    power=power>>1
print(ans)
