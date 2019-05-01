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
            
