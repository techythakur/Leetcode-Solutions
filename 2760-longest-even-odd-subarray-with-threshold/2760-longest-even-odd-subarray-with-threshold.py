class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans, cnt = 0, 0

        for i, num in enumerate(nums):

            if num > threshold:
                cnt = 0

            elif cnt and parity != num%2:
                parity^= 1
                cnt+= 1

            else:
                parity = num%2
                cnt = parity^1

            ans = max(ans, cnt)

        return ans