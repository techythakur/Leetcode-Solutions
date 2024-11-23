class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        curr = 0
        maxm = 0
        while l<r:
            if height[l]>height[r]:
                curr = height[r] * (r-l)
                r-=1
            else:
                curr = height[l] * (r-l)
                l+=1
            maxm = max(curr,maxm)
        return maxm