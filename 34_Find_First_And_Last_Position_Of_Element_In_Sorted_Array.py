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
