from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sheap = []
        self.lheap = []  
        # slen, llen = 0, 0
        

    def addNum(self, num: int) -> None:
        if len(self.sheap) == len(self.lheap):
            heappush(self.lheap, - heappushpop(self.sheap, -num))
        else:
            heappush(self.sheap, - heappushpop(self.lheap, num))

    def findMedian(self) -> float:
        if len(self.sheap) == len(self.lheap):
            return float(self.lheap[0] - self.sheap[0])/2.0
        else:
            return float(self.lheap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
