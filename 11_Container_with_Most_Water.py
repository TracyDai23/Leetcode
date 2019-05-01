# Own solution get time limit exceed result. 
# Other's solution is an O(N) solution with reasonable logic method. 

# own solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        d = dict(enumerate(height))
        a = amax = 0
        # print(d)
        md = len(height)/2 # mean of distance
        mh = sum(height)/len(height) # mean of vertical line height
        print(md, mh)
        # print(d)
        l = 0 
        r = len(height)-1
        
        
        while r >= md-1:
            l=0
            while l <= r:
                if d[l] >=mh and d[r]>= mh and r-l >= md:
                    a = min(d[l],d[r])*abs(r-l)
                    amax= max(a,amax)
                    # print('case 1:',l, r, d[l],d[r],amax)
                l+=1
            r-=1
        if amax >0:
            return amax
        else:
            r = len(height)-1
            while r >= md-1:
                l=0
                while l<=r:
                    if (d[l]+d[r])/2>= mh or r-l>= md-1:
                        a = min(d[l],d[r])*abs(r-l)
                        amax= max(a,amax)
                        # print('case 2:',l, r, d[l],d[r],amax)
                    l+=1
                r-=1
        
        return amax
  
  # Other's solution:
  class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        w=0
        a = amax = 0
        for w in range(len(height)-1,0,-1):
            a = min(height[l],height[r])*w
            amax = max(amax,a)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        
        
        return amax
