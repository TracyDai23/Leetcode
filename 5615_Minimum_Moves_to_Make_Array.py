from statistics import mode, median
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        s = [] 
        n = len(nums)
        for i in range(len(nums)//2):
            s.append(nums[i] + nums[n-1-i])
        
        
        # corner case: already complementary
        allEqual = True
        for i in range(len(s)):
            if s[i] != s[0]:
                allEqual = False
        if allEqual:
            return 0
        
                
        
        # Function: findChange: return 1 or two for moves needed. 
        def findChange(target):
            for i in range(len(s)):
                cnt = 0
                if s[i] != target:
                    if target/2 > limit:
                        return -1
                    elif target >limit and  target - max(nums[i], nums[i-n-1])>limit:
                        cnt += 2
                    else:
                        cnt +=1
                print(target, cnt)
                return cnt
                        
               
        
        s = sorted(s)
        l = 0
        r = len(s) -1
        res = 1000000
        while l <= r:
            mid = (l+r)//2
            target = s[mid]
            tmp = findChange(target)
            if tmp != -1:
                res = min(res, tmp)
                l = mid +1
            else:
                r = mid-1
        return res
    
        
            
        
