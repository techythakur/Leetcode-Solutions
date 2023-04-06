class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.isClosedIsland(grid, i, j):
                    count += 1
        
        return count

    def isClosedIsland(self, grid: List[List[int]], i: int, j: int) -> bool:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        
        if grid[i][j] != 0:
            return True
        
        grid[i][j] = 2
        
        res = True
        res &= self.isClosedIsland(grid, i-1, j)
        res &= self.isClosedIsland(grid, i+1, j)
        res &= self.isClosedIsland(grid, i, j-1)
        res &= self.isClosedIsland(grid, i, j+1)
        
        return res