import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
            if dic[i] > math.floor(len(nums)/2):
                return i
        return -1