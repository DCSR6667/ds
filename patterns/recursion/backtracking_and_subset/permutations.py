'''this can be done by subset pattern--(processing/unprocessing)'''
'''second approach is by swaping and backtracking approach'''
def permutation(ans,s):
    if len(s)==0:
        print(ans)
        return
    size=len(ans)+1
    ch=s[0]
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        permutation(first+ch+last,s[1:])


def permutation1(ans,s):
    if len(s)==0:
        l=[]
        l.append(ans)
        return l
    size=len(ans)+1
    ch=s[0]
    lis=[]
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        lis=lis+permutation1(first+ch+last,s[1:])
    return lis

def permutation2(ans,s,l):
    if len(s)==0:
        l.append(ans)
        return l
    size=len(ans)+1
    ch=s[0]
    for i in range(size):
        first=ans[0:i]
        last=ans[i:size]
        permutation2(first+ch+last,s[1:],l)
    return l
print(permutation2("","abc",[]))


class Solution:
    def arrange(self,nums,i,l):
        if i==len(nums):
            l.append(nums.copy())
            return l
        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            self.arrange(nums,i+1,l)
            nums[i],nums[j]=nums[j],nums[i]
        return l
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.arrange(nums,0,[])
        


