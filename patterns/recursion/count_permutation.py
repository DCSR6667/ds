'''this can be done by subset pattern--(processing/unprocessing)'''
def count_permutation(ans,s):
    if len(s)==0:
        return 1
    size=len(ans)+1
    ch=s[0]
    count=0
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        count=count+count_permutation(first+ch+last,s[1:])
    return count

print(count_permutation("","abc"))