def min_max(l):
    min,max=l[0],l[1]
    for i in range(2,len(l)):
        if l[i]>max:
            max=l[i]
        elif l[i]<min:
            min=l[i]    
    return min,max
print(min_max([-2,5,4,7,-1,2,8]))