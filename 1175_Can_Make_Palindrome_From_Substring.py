class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        def checkPalidrome(string, k):
            mdict = {}
            for i in range(len(string)):
                if string[i] in mdict:
                    mdict.pop(string[i])
                else:
                    mdict[string[i]] =1
            # print(mdict, len(mdict),k)
            if len(mdict)%2 ==0 and len(mdict)<=k*2:
                return True
            elif len(mdict)%2 == 1 and len(mdict)<=k*2+1:
                return True
            else: 
                print('elseFalse')
                return False
        
        res=[]
        for query in queries:
            if s[query[0]:query[1]+1] == s[query[0]:query[1]+1:-1]:
                res.append(True)
            # print(s[query[0]:query[1]+1])
            else:
                res.append(checkPalidrome(s[query[0]:query[1]+1],query[2]))
        return res
