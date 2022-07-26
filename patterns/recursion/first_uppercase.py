def first(s,i):
    if i>=len(s):
        return -1
    if s[i].isupper():
        return s[i]
    return first(s,i+1)

print(first("chandra",0))