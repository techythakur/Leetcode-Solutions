class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        for col, row in stones:
            rows[col].append(row)
            cols[row].append(col)

        # Group all stones using DFS
        # Initialzie a set to keep track of visited stone
        visited = set()

        # Initialize a number of group found
        group = 0

        # Iterate through all stones
        for col, row in stones:

            # If we already visited the current stone, skip it
            if (row, col) in visited:
                continue

            # Else, we have found a new group
            group += 1

            # Add the current stone into the stack
            stack = [(row, col)]
            visited.add((row, col))

            # Iterate until stack is empty
            while stack:

                # Pop a stone
                row, col = stack.pop()

                # Add all unvisited stones at the same col into the stack
                for nRow in rows[col]:
                    if (nRow, col) not in visited:
                        visited.add((nRow, col))
                        stack.append((nRow, col))

                # Add all unvisted stones at the same row into the stack
                for nCol in cols[row]:
                    if (row, nCol) not in visited:
                        visited.add((row, nCol))
                        stack.append((row, nCol))

        # Return the number of removed stones
        return len(stones) - group