class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sumleft, sumright, lengthright, lengthleft, min, ind, = 0, sum(nums), len(nums), 0, 9999999, 0
        for i in range(len(nums)):
            sumleft += nums[i]
            sumright -= nums[i]
            lengthleft+=1
            lengthright-=1
            if lengthright!=0:
                val = (abs(sumleft//lengthleft - sumright//lengthright))
            else:
                val = (abs(sumleft//lengthleft))
            if val<min:
                min=val
                ind = i
        return ind