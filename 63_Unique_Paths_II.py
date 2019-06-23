#My first trial:

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*(n+1)]*(m+1)
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        if obstacleGrid[-1][-1] ==1:
            return 0
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]
        return dp[-1][-1]
    
