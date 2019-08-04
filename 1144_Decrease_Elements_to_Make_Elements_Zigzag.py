# wrong answer
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        move_e, move_o = 0,0
        even,odd = [],[]
        
        
        for i in range(0,len(nums),2):
            if nums[i]:
                even.append(nums[i])
            if nums[i+1]:
                odd.append(nums[i+1])
        print(even, odd)
        for j in range(len(nums)//2):
            if len(nums)%2 == 0:
                even.append(1001)
            # check even > odd
            if odd[j]>=min(even[j],even[j+1]):
                move_e += min(even[j],even[j+1]) - odd[j]+1
        
        for j in range(len(nums)//2):
            if j ==0 and even[j] >=odd[j]:
                move_o = odd[j]-even[j]+1
            #elif: j == len()
            else:
                # check even < odd
                if even[j]>=min(odd[j-1],odd[j]):
                    move_o +=min(odd[j-1],odd[j]) -even[j] + 1
            if move_o>move_e:
                break
        return min(move_e,move_o)
