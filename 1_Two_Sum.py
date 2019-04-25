# 37.8% 
# 这道题，我的痛点居然是不知道怎么检查“如何不用同一个数字两次”  TEST CASE: nums = [3,3], target = 6
# take-away: 需要直接interpret 条件


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            b = target - nums[i]
            if b in nums and nums.index(b) != i:
                return sorted([i, nums.index(b)])
                
        return []
        
# Other's solutions: 
# key words: enumerate, dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        for index_1, num_1 in enumerate(nums): # 同一个数不适用两遍是通过index_1的for loop实现的
            #print (lookup)
            if target - num_1 in lookup:
                return [index_1, lookup[target-num_1]]
                break
            lookup.update({num_1:index_1})
