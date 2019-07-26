class Solution:
    def numSquares(self, n: int) -> int:
        # Find perfectList 
        perfectList = []
        i=1
        while i**2 <=n:
            perfectList.append(i**2)
            i+=1
        # print(perfectList)
        perfectList = perfectList[::-1]
        
        #Initialize DP map
        dp=[0]*(n+1)
        
        #Edge case: when it's perfectList number, the count of numbers needed are 1.
        for num in perfectList:
            dp[num] = 1
        
        # DP main portion:
        for residue in range(n+1): # fill in all DP result from 1 to n
            nummin = residue # initialize number of perfect number needed can always be n*1, so residue*1
            for j in [c for c in perfectList if c<=residue]: # check every possible perfect number in perfectList
                if dp[residue-j]+1 < nummin: # check if new method number count +1 is less than previous minimum number of perfects("nummin"), update it. 
                    nummin = dp[residue-j] + 1
            dp[residue] = nummin # when all possible combination has checked, apply nummin to the dp map.
        # print(minNumb)
        return dp[n]
