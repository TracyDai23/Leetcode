# Wrong answer attempt, still need to work on the i,j looping part.
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        dp = [0]*len(matrix)
        prev = 0
        rmax = 0
        for i in range(len(matrix[0])):
            prev = 0
            for j in range(len(matrix)): 
                prev_new = dp[j]
                if j-1 <0:
                    dp[j-1] = 0
                if matrix[i][j] == '1':
                    dp[j] = min(prev, dp[j-1],dp[j])+1
                else:
                    dp[j]= 0
                prev = prev_new
            if rmax < max(dp):
                rmax = max(dp)
        return rmax*rmax
