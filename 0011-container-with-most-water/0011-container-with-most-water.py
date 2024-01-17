class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area = 0
        maxarea = 0
        while i<j:
            if height[j]>height[i]:
                area = height[i]*(j-i)
                i+=1
            else:
                area=height[j]*(j-i)
                j-=1
            maxarea = max(area, maxarea)
        return maxarea
                