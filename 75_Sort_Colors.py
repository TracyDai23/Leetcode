# After review other's video. I am able to repeat the solution in Python. 
# 95.89% time complexity: O(N)
# space complexity: constant space
# solutin 1 is 1)two pointers, 2) one pass, 3) modify array order in-place.
# solution 2 is a two passes solution, count number of variables and rewrite object.

#Solution 1:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution 1: 
        #aa | bb| xxx|c
        # i: beginning of b 
        # j: beginning of x
        # k: end of x
        # [j,k] unknown list
        
        if not nums:
            return 
        
        i,j,k=0,0,len(nums)-1
        
        while j <=k:
            if nums[j] == 0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j] == 1:
                j+=1
            elif nums[j] == 2:
                nums[k],nums[j]=nums[j],nums[k]
                k-=1
            else:
                continue
        
        # print(nums)
            
# Solution 2: two passes, count and then rewrite object.
# Time complexity: O(N), counter should be O(log(N)).
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt=dict(collections.Counter(nums))
        if not nums:
            return
        k = len(nums)
        
        i=0
        while i < cnt.get(0,0):
            nums[i] = 0
            i+=1
        while i < cnt.get(1,0)+cnt.get(0,0):
            nums[i] = 1
            i+=1
        while i <k:
            nums[i] =2
            i+=1
        # print(nums)
