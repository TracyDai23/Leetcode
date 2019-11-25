# Time: O(NlogN) because sort is O(NlogN) and in worst case, the heappush will be N times of O(logN) action.

from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        
        heap = [intervals[0][1]]
        for i in intervals[1:]:
            if heap[0]<= i[0]:
                heappop(heap)
            heappush(heap, i[1])
        
        return len(heap)
        
