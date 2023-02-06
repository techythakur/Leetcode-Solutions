class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        y=[]
        for i in range(len(nums)):
            if i>n-1:
                y.append(nums[i])
            else:
                x.append(nums[i])
        res=[]
        for i in range(n):
            res.append(x[i])
            res.append(y[i])
        return res