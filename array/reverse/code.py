def reverselist(l,i,j):
    if i<j:
        l[i],l[j]=l[j],l[i]
        reverselist(l,i+1,j-1)
    else:
        return
l=[1,2,3,4,5]
reverselist(l,0,4)
print(l)




