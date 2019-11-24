# 找maximum 的题， 还是需要用-value然后最后从heap里取top k， 而不需要要求heap里只有top k 个元素。 heap里对元素数量的要求是295， find median的题型

from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        print(d)
        h = []
        
        for key,value in d.items():
            h.append((-value, key))
        heapify(h)
        return [heappop(h)[1] for _ in range(k)]
