class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for idx,val in enumerate(prices):
            for j in range(idx+1, len(prices)):
                if val>=prices[j]:
                    prices[idx] = val - prices[j]
                    break
        return prices
            