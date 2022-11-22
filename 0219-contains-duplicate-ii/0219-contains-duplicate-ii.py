class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in last_seen:
                if i - last_seen[x] <= k:
                    return True
            last_seen[x] = i
        return False