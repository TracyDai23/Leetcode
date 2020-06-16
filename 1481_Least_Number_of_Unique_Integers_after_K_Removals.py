# Incorrect answer from contest
class Solution:
    
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        print(len(arr))
        def rSum(l):
            res = 0
            for item in l:
                res += item[1]
            return res
    
        
        d = collections.Counter(arr)
        if k == 0:
            return len(d)
        # print(d)
        d2 = collections.Counter(d.values())
        print(d2)
        res = [(i,d2[i]) for i in d2]
        res.sort()
        print(res)
        r = []
        while k>0 and len(res)>0:
            tmp = res[0][1]*res[0][0]
            # print(tmp,k)
            if k> tmp:
                print("1")
                k -= res[0][1]
                res = res[1:]
            elif k == tmp:
                print("2")
                return rSum(res[1:])
            else:
                if k >= res[0][0]:
                    print("3")
                    res[0] = (res[0][0],res[0][1]-int(k/res[0][0]))
                    print(res)
                    return rSum(res)
                else:
                    print("4")
                    return rSum(res)
        return 0
        
        

                
