class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        lp = 0
        rp = 1
        rsum = cost[lp]
        rmax = cost[lp]
        count = 0
        res = 0
        while rp < len(s):
            # print("lp, rp, rmax, rsum: ", lp, rp, rmax, rsum)
            if s[lp] == s[rp]:
                rmax = max(rmax, cost[rp])
                rsum += cost[rp] 
                rp +=1
            else:
                # first to resolve any pending repeating letter issue:
                res += (rsum-rmax)
                # then reset to new letter
                lp =rp
                rp +=1
                rsum, rmax = cost[lp],cost[lp]
        res += (rsum-rmax)
        return res
                
        
