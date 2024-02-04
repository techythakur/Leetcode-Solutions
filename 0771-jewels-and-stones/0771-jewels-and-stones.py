class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel_list = list(jewels)
        for i in jewel_list:
            count += stones.count(i)
        return count