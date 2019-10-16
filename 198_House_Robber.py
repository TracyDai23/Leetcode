# DP 
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rmax = 0
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        
        dp = [None]*(len(nums))
        dp[0]= nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            rmax = max(rmax, dp[i])
        
        
        return rmax