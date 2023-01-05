class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        tally, bow = 1, points[0][1]
        for start, end in points:
            if bow < start:
                bow = end
                tally += 1     
        return tally    