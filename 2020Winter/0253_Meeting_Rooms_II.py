# Mysolution
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        if not intervals[0]: return 1
        
        # step 1: sort by start time
        intervals = sorted(intervals)
        # print(intervals)
        
        res = [0]
        # step 2: allocate meeting room:
        for i in range(len(intervals)):
            if intervals[i][0]>= min(res):
                m = min(res) # 这里改成用heap可以提高performance
                res.remove(m)
                res.append(intervals[i][1])
                # print('op1: round:', i, res)
            else:
                res.append(intervals[i][1])
                # print('op2: round:', i, res)
        return len(res)
                
        
