# My first thought, but did not finish
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d = collections.defaultdict(list)
        for point in points:
            dis = point[0]**2 + point[1]**2
            d[dis].append(point)
            print(d)
        kmin = min(d.keys())
        return d[kmin]
        
# Sort: O(nlogn); O(n)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda p: p[0]**2 + p[1] ** 2)
        return points[:K]
        
#Heap： O(nlogk); O(k)
