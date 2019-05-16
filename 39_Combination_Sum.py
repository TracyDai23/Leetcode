# My own solution: 10% backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def trec(t,c=[]):
            if t == 0:
                if sorted(c) not in result:
                    result.append(sorted(c))
                return
            for d in candidates:
                # print(d,t)
                if d<=t:
                    trec(t-d,c+[d]) #within function, cannot use method, can only use basic operators.
        trec(target,[])
        return result

# Other's solution: the same logic as mine.  68.94%

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        def trec(t,c=[]):
            if t == 0:
                # if sorted(c) not in result:
                result.append(c)
                return
            for d in candidates:
                # print(d,t,c)
                if d >t:break # This line will break the whole FOR loop when candidate is larger than target
                if c and d <c[-1]: continue # this line will continue to the next candidate to exclude results with no need to sort and exclude. 
                else:
                    print('processed')
                    trec(t-d,c+[d]) #within function, cannot use method, can only use basic operators.
        trec(target,[])
        return result
