# 2nd try with dictionary: 23.59% 
# take-aways: rst = list(dict.fromkeys((map(tuple, rst)))) # remove duplicates from list
# Other's solution: O(n*n), used two pointer, and very similar to question 11


# 1st try: time limit exceed
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l,r,rst, cl=0,0,[],[]
        while nums:
            if nums[0] in cl:
                nums.pop()
            else:
                c=nums.pop()
                cl.append(c)
                n=nums
                while n:
                    a,n=n[0],n[1:]
                    b = -c-a
                    # print('nums,n,c,a,b:', nums,n,c,a,b)
                    if b in n and sorted([a,b,c]) not in rst:
                        rst.append(sorted([a,b,c]))
        return rst
            
# Use dictionary to simplify time complexity:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l,r,rst, cl=0,0,[],[]
        while nums:
            if nums[0] in cl:
                nums.pop(0)
            else:
                c=nums.pop(0)
                cl.append(c)
                lookup = {} # list value dictionary after go through the number
                for index_1,a in enumerate(nums): # enumerate provides index and value
                    if -c-a in lookup:
                        rst.append(sorted([a,-c-a,c]))
                    lookup.update({a:index_1})
        rst = list(dict.fromkeys((map(tuple, rst)))) # remove duplicates from list
        
        return rst

    
# Other's solution: two pointer, O(n*n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: #ignore duplicate elements
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r])) # when s == 0, then it's a solution.
                    while l < r and nums[l] == nums[l+1]: # ignore duplicate elements on left end
                        l += 1
                    while l < r and nums[r] == nums[r-1]:# ignore duplicate elements on right end
                        r -= 1
                    l += 1; r -= 1 # move pointer.
        return res 
