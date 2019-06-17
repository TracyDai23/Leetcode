# copied solution from others
# 这个题的问题是没有能够仔细的把思路用代码写完。这个问题比较严重，因为总是依赖看答案和精简思路，代码执行能力有点问题。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # start = [0,0]
        # ms=[]
        # for i in range(len(intervals)):
        #     if intervals[i][1]>= intervals[i+1][0]:
        #         #思路： 查当前list的后数是不是大于等于前数。如果是
        
        intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        for i in range(len(intervals)):
            if res and intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res += [intervals[i]]
        return (res)
                
