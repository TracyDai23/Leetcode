# 2nd try with dictionary: 23.59% 
# take-aways: rst = list(dict.fromkeys((map(tuple, rst)))) # remove duplicates from list

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
