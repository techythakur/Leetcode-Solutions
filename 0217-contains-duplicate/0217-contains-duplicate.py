class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        has = {}
        for i in nums:
            if i in has:
                return True
            else:
                has[i]=1
        return False