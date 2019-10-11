class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        l = len(nums)
        
        for (key,value) in d.items():
            if value > l/2:
                return key
            
        
