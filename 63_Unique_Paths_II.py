
# My submission: 跟官方答案的思路一致，就是需要初始化第一行和第一列，然后中间部分可以通过move计算。
# Time complexity: O(N), 89.67%
# Space complexity: O(N)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0]*n
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] ==1:
            return 0
        
        # initial case: dp[0][j]
        if obstacleGrid[0] != 1:
            dp[0] = 1
        for j in range(1,n):
            if obstacleGrid[0][j] != 1:
                dp[j] = dp[j-1]
        
        for i in range(1,m):
            # initialize dp[i][0]
            if obstacleGrid[i][0]==1:  dp[0] = 0
            else: dp[0] = dp[0]
                
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j]+dp[j-1]
        return dp[-1]

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
    
