import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            maxHeap.append(-s)
        
        heapq.heapify(maxHeap)
        while(len(maxHeap) >1):
            diff = abs(heapq.heappop(maxHeap) - heapq.heappop(maxHeap))
            heapq.heappush(maxHeap, -diff)
        
        return -maxHeap[0]
