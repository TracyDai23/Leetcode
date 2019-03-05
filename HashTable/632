# Condition: 1) smallest range includes at least one number from each of the k lists; 2) if two ranges equals, use the one with smaller a.

#test cases:
[[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]


# 0,4,5,9,10,12,15,18,20,22,24,26,30
 # Thought DongDong: 1)Merge all sublist into one big sort list; 
              2)loop range and check if all list contain at least one number in this range, and flag. e.g. range= (0,4)
              3)Then increase step from 1 to 2, check range = [0,5] and if contains. And then keep on loop [point, point +step]
              4)Exit when all ranges checked and return saved samllest range.
              
 # Thought 1: 
# Condition: 1) smallest range includes at least one number from each of the k lists; 2) if two ranges equals, use the one with smaller a.

# 0,4,5,9,10,12,15,18,20,22,24,26,30
 # Thought 1: 

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        p = [0]*len(nums)
        for i in range(len(nums)):
                p[i] = len(nums[i])-1
        # print('p: ',p)
        sr=[-100000,200000]
        
        def calculateRange(alist):
            m = min(alist)
            x = max(alist)
            r = [m,x-m] #range[0] is range start point, range[1]is rangewide
            return r
        def movePointer(m,x,p,nums):
            no_move =0
            m=int(m)
            x=int(x)
            for i in range(len(p)):
                    if m< nums[i][p[i]-1] <= x:
                        if p[i]>0:
                            p[i]=p[i]-1
                            no_move =1

            if no_move==0:
                    for i in range(len(p)):
                            if p[i]>0:
                                    p[i] = p[i]-1
            return p
        
        while sum(p)>0: #p location index counts from largest to smallest.
                newList = []
                for i in range(len(nums)):
                        newList.append(nums[i][p[i]])
                        i=i-1
                #For loop finished the preparation of newList input for calculate function.
                print('current_newList: ',newList)

                # Calculation starts from here
         
                cr=calculateRange(newList)
                print('current_range: ',cr)
                x=sum(sr)
                p=movePointer(sr[0],x,p,nums)
                print('currnet_pointer: ',p)
                if sr[1]>cr[1] or (sr[1]==cr[1] and sr[0]>cr[0]):
                        sr=cr
                print('current smallest range: ',sr)
        while sum(p)==0:
                newList = []
                for i in range(len(nums)):
                        newList.append(nums[i][0])
                        i = i-1
                print('current_newList: ',newList)      
                cr = calculateRange(newList)
                print('current_range: ',cr)
                if (sr[1]>cr[1] or (sr[1] == cr[1] and sr[0]>cr[0])):
                        sr=cr
                print('current smallest range: ',sr)
                break
        srange =[sr[0],sr[0]+sr[1]]
        return srange

    
