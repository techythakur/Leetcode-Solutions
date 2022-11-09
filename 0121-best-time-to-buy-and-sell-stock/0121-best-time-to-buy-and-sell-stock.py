class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        maxp=0
        p=0
        while right<len(prices):
            if prices[left]<=prices[right]:
                p=prices[right]-prices[left]
                maxp=max(maxp,p)
            else:
                left=right
            right+=1
        return maxp