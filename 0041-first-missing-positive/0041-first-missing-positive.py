class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset=set(nums)
        for i in range(1,len(nums)+1):
            if i in hashset:
                continue
            else:
                return i
        return len(nums)+1