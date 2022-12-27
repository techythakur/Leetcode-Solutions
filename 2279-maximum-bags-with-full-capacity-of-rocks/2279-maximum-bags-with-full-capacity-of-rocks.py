class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left=[0]*len(rocks)
        for i in range(len(rocks)):
            left[i]=capacity[i]-rocks[i]
        left.sort()
        c=0
        for i in left:
            if(i<=additionalRocks):
                c+=1
                additionalRocks-=i 
        return c
    