# Referred to discussion

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        small = nums[0]
        big = nums[0]
        smax= nums[0]
        
        for i in  range(1,len(nums)):
            small, big = min(nums[i], nums[i]*small, nums[i]*big ), max(nums[i], nums[i]*small, nums[i]*big )
            smax = max(smax, big)
        
        return smax
            
        
