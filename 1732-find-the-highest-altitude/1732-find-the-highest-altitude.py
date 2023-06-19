class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr=[0]
        alt=0
        for i in range(len(gain)):
            alt+=gain[i]
            arr.append(alt)
        return max(arr)