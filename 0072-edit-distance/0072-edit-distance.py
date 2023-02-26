class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0] * (len2+1) for i in range(len1+1)]
        for i in range(len1):
            dp[i][-1] = len1 - i
        
        for i in range(len2):
            dp[-1][i] = len2 - i

        
        for r in range(len1-1, -1, -1): # bottom up
            for c in range(len2-1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                    
                else:
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1]) 
        
        return dp[0][0]