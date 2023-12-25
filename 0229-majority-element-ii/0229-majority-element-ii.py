from collections import *
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        count = Counter(nums)
        for i,j in count.items():
            if j>math.floor(len(nums)/3):
                result.append(i)
        return result