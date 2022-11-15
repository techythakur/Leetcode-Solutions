import math
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        cnt=0
        n=len(nums)
        for i in range(n):
            lcm=nums[i]
            if lcm==k: cnt+=1
            for j in range(i+1,n):
                gcd=math.gcd(lcm,nums[j])
                lcm=(lcm*nums[j])//gcd    #lcm(a,b) * gcd(a,b) =a*b
                if lcm>k:
                    break
                if lcm==k:
                    cnt+=1
        return cnt