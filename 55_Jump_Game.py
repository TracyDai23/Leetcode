# 97%
# 这个题目的痛点在于逻辑分析完以后，实现方法上的loop flow没有理清楚。 包括1）把一个corner case 当成一个scenario在讨论（line17）；
# 2）然后flag的设置和break，continue的跳出loop的方式和范围理解不清楚； 3） line 32的这种方式没有想到，总想着简化

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #reverse nums and check zero
        if len(nums)<=1:
            return True
        if 0 not in nums:
            return True
        if nums[0]==0:
            return False
        nr=nums[::-1]
        # print(nr)
        
        # when has number before 0, then check if after consecutive zero has number longer than distance+1
        # when no number befoer 0, then check if after consecutive zero has number longer than distance #This is a corner case, no need to treat as a separate scenario.
        check = True
        for i in range(1,len(nr)):
            if nr[i] ==0:
                check = False
                n=i+1
                while n<len(nr):
                    # print( i, n,nr[n],n-i)
                    if nr[n]> n-i:
                        check = True 
                        break
                    else:
                        n+=1
                        continue
                if not check: # if check is false when finish a "0" check, then return False directly
                    return check

                    
            
                        
        return check
