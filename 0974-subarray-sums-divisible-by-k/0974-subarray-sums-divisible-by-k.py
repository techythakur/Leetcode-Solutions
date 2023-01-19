class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        l=len(nums)
        remainders={0:1}
        pre=0
        total=0
        for i in range(l):
            pre+=nums[i]
            rem=pre%k
            remainders.setdefault(rem,0)
            total+=remainders[rem]
            remainders[rem]+=1
            
        return total