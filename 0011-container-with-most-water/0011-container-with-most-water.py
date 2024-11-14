class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        area,maxarea = 0,0
        while i<j:
            if height[j]>height[i]:
                area = height[i]*(j-i)
                i+=1
            else:
                area = height[j]*(j-i)
                j-=1
            maxarea = max(maxarea, area)
        return maxarea
                
        