# My own solution: 94.15%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst=[]
        n =len(nums)
        def trec(c=[],snum=nums):
            if len(c) ==n:
                rst.append(c)
                return 
            snum = list(set(nums)-set(c)) # Get difference elements from two lists.
            for d in snum:
                trec(c+[d], snum[1:])
        trec()    
        return rst
                


# Referred to other's solution, passed snum directly from trec() function. 
# 36.84%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst=[]
        n =len(nums)
        
        def trec(c=[],snum=nums):
            if len(c)==n:
                rst.append(c)
                return 
            # snum = list(set(nums)-set(c))
            for i in range(len(snum)):
                trec(c+[snum[i]], snum[:i]+snum[i+1:])
        trec()    
        return rst
