def dice(ans,target,face):
    if target==0:
        print(ans)
        return 
    i=1
    while i<=face and i<=target:
        dice(ans+str(i),target-i)
        i+=1

def dice1(ans,target,face):
    if target==0:
        l=[]
        l.append(ans)
        return l 
    li=[]
    i=1
    while i<=face and i<=target:
        li=li+dice1(ans+str(i),target-i,face)
        i+=1
    return li

def dice2(ans,target,l,face):
    if target==0:
        l.append(ans)
        return l
    i=1
    while i<=face and i<=target :
        dice2(ans+str(i),target-i,l,face)
        i+=1
    
    return l

print(dice2("",5,[],6))
