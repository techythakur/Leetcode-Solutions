class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ans = 0
        n = len(ages) 
        dp = [0] * n  
        temp = []  
        for i in range(len(scores)): 
            temp.append([-ages[i], -scores[i]]) 
        temp.sort()
        for i in range(n):
            for j in range(i, -1, -1):
                if -temp[i][1] <= -temp[j][1]:
                    dp[i] = max(dp[i], dp[j]-temp[i][1]) 
            ans = max(ans, dp[i])
        return ans