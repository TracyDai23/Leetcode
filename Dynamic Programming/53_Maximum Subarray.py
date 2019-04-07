#Dongdong's solution: 93.77%

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum = nums[0]
        temp_sum = 0
        for item in nums:
            temp_sum = temp_sum + item
            if temp_sum > maximum:
                maximum = temp_sum
            if temp_sum < 0:
                temp_sum = 0
                
        return maximum

# My solution: 28%
# find the max positive number, and then add all positive two sum (tsum)  from max number position
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max= nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):

            if sum <0:
                sum = nums[i]
            else:
                sum = sum+nums[i]
            if sum > max:
                max = sum
        return max
