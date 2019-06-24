# My own solution: 95.45%
# DP: time complexity: O(N), space complexity: O(N)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        
        dp=[0]*n
        for j in range(0,n):
            dp[j] = dp[j-1]+grid[0][j]
            
        for i in range(1,m):
            dp[0] = grid[i][0]+dp[0]
            for j in range(1,n):
                dp[j]=grid[i][j]+min(dp[j],dp[j-1])
            # print(dp)
        return dp[-1]
