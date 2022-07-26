def remove(s,i,l):
    if i==len(s)-1:
        l=l+s[i]
        return l
    if s[i]!=s[i+1]:
        l=l+s[i]
    return remove(s,i+1,l)

#without any space
def remove1(s):
    if len(s)<=1:
        return s
    if s[0]!=s[1]:
        return s[0]+remove1(s[1:])
    else:
        return remove1(s[1:])
   
   


print(remove1("geeksforgeeks"))