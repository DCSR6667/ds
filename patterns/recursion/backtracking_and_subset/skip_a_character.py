def skip(s,ans,ch):
    if len(s)==0:
        return ans
    if s[0]!=ch:
        ans=ans+s[0]
    s=s[1:]
    return skip(s,ans,ch)

print(skip("chandra","","a"))
    
