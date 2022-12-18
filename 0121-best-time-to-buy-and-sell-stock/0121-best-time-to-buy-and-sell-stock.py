class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        profit=0
        maxprofit=0
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxprofit=max(profit,maxprofit)
            else:
                left=right
            right+=1
        return maxprofit
        