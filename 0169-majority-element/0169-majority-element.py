from collections import *
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i,j in count.items():
            if j>math.floor(len(nums)/2):
                return i
        return -1