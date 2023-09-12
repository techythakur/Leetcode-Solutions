class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        has={}
        for i in nums:
            if i not in has:
                has[i]=1
            else:
                has[i]+=1
        
        for i,j in has.items():
            if j>=2:
                return True
        return False