def skip(s,ans,skipstr):
    if len(s)==0:
        return ans
    if not s.startswith(skipstr):
        ans=ans+s[0]
        s=s[1:]
        return skip(s,ans,skipstr) 
    else:
        s=s[len(skipstr):]
        return skip(s,ans,skipstr)

print(skip("chandrasekhar","","chandra"))
