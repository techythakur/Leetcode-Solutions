class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise and hare's algo or Floyds cycle finding algo
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:    # detects the cycle in the array
                break
        fast = nums[0]
        while slow != fast:    # get fast to the duplicate array by resetting fast
            slow = nums[slow]
            fast = nums[fast]
        return fast
    
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return i
        #     s.add(i)
        # return False