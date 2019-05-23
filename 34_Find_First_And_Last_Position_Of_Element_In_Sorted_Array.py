# Corrected submission: binary search  
# time complexity: O(log n) 86%
#space complexity: O(1) per official solution. All work is done in place, so the overall memory usage is constant.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==0:
            return [-1,-1]
        L,H,S,E = 0, len(nums)-1,-1,-1
        if len(nums) == 1:
            if nums[L]==target:
                return [L,H]
            else:return [-1,-1]
        
        while L<=H:
            M= (L+H)//2
            print('L,H,S,E,M:',L,H,S,E,M)
            if nums[M] == target:
                S=E=M
                L,H=M-1,M+1
                break
            elif nums[M] < target:
                L=M+1
            else:
                H=M-1
        if S!=-1:
            while L>=0 and nums[L] == target:
                S=min(S,L)
                L-=1
            while H<= len(nums)-1 and nums[H] ==target:
                E=max(E,H)
                H+=1
        return [S,E]
        

# My first attempt with index exceed issue:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L,H,S,E = 0, len(nums)-1,-1,-1
        while L<H:
            M= (L+H)//2
            print('L,H,S,E,M:',L,H,S,E,M)
            if nums[M] > target:
                H=M
            elif nums[M] < target:
                L=M+1
            elif nums[M] == target:
                if S==-1:
                    S=E= M
                    L,H=M-1,M+1
                break
                # while nums[L] == target:
                #     S=min(S,L)
                #     L-=1
                # while nums[H] == target:
                #     E=max(E,H)
                #     H+=1
            else:
                continue
        while nums[L] == target:
            S=min(S,L)
            L-=1
        while nums[H] ==target:
            E=max(E,H)
            H+=1
        return [S,E]
