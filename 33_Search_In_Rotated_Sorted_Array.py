# Other's solution: 98.7%
# 这个二分法的题是直接用iteration做的。 nums是一个有序，但是位置有一个调整的list。 
# 所以，用数学方法讨论和处理这个调整（drop），就可以完成这道题的binary search。不需要recursion。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if nums[M] < nums[0] <= target: # +inf
                H = M
            elif nums[M] > nums[0] > target: # -inf
                L = M+1
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1



# My original codes with no submission result.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(alist,t):
            l=r=0
            if len(alist) == 0:
                return False
            else:
                midpoint = len(alist)//2
                if alist[midpoint] ==t:
                    print('new round: ',alist,midpoint)
                    return r
                else:
                    if t <alist[midpoint]:
                        r+=midpoint
                        print('move r:',r)
                        return binarySearch(alist[:midpoint],t)
                    else:
                        l+=midpoint
                        return binarySearch(alist[midpoint+1:],t)
                    
        
        
        #step 1: use binary search to find cut point
        cp = midpoint = len(nums)//2
        print(midpoint)
        while cp:
            if cp == len(nums)-1 or cp == 0:
                cp ==0 
            
            elif (nums[cp]-nums[cp-1])<0:
                break
            elif nums[cp]<nums[-1]:
                cp-=1
            else:
                cp+=1
        
        #step 2: use binary search to locate target
        # def binarySearch(midp,t)
        alist = nums[cp:]+nums[:cp]
        print(alist)
        position = binarySearch(alist,target)
        print(position)
            
            
