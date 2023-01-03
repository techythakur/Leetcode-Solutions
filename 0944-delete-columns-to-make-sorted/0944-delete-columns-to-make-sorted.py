class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n_rows, n_cols, n_del = len(strs), len(strs[0]), 0
        for j in range(n_cols):
            col_sorted = True
            for i in range(n_rows-1):
                if strs[i][j]>strs[i+1][j]:
                    col_sorted = False
                    break
            if not col_sorted:
                n_del += 1
        return n_del  