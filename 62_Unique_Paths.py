# 计数题通常都是动态规划。
# 很好的recursion 和 DP 思路说明： https://www.youtube.com/watch?v=fmpP5Ll0Azc

# My own solution: Time limit exceed.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #使用back tracking， right有m个机会，down有n个机会。看有多少种组合方法
        
        self.cnt = 0
        self.pth = [] # try to record path, and deduplicate path
        
        def rec(m,n,suba=[]):
            
        # if n<= 0 or m <= 0:
        #     return
            if n == 0 and m == 0: #and suba not in self.pth:
                self.pth.append(suba)
                self.cnt+=1
                return
            if n >0:
                rec(m,n-1,suba+['d'])
            if m>0:
                rec(m-1,n,suba+['r'])
        
        rec(m-1,n-1)
        return self.cnt


# Dynamic Programming solution：
# Time complexity: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      if not m or not n:
        return 0
      dp = [[1]*n]*m]
      for i in range(1, m):
        for j in range(1, n):
          dp[i][j] = dp[i-1][j] + dp[i][j-1]
      return dp[-1][-1]
      
# Optimized DP:
# 因为上一个答案的dp[i-1][j]，实际上是存储在当前dp[i][j]里面的。所以只需要一维数组就可以完成line37的计算。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      if not m or not n:
        return 0
      rec=[1]*n
      for i in range(1, m):
        for j in range(1, n):
          rec[j] = rec[j] + rec[j-1]
      return rec[-1]
