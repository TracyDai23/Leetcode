# First trial, not correct yet. Tried to use backtracking

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False]*len(s)
        res = []
        #step1: 
        def trec(dp, i=0, array=[]):    
            print('new round: ',dp, i, array,res)
            # base case: if dp[-1]  then append the result
            if dp[-1]:
                res.append(array[1:])
                dp = [False]*len(s)
                return
            
            #main checking
            for word in wordDict:
                print(word,dp, i, array)
                if word == s[i: len(word)+i] and (dp[i-1] or i==0):   
                    dp[i+len(word)-1] = True
                    array= array + ' '+word
                    print('hit: ', dp, i, array)
                    trec(dp,i+len(word),array)
        
        # while wordSearch
        trec(dp,0,'')
        return res
            
                
        
