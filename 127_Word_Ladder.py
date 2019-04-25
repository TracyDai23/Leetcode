# My 1st try. Exceed Time Limit, but able to provide correct result. 
# Dongdong's solution is accepted. Other optimization includes "bidirectional BFS" for next try.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        vq = [beginWord] #current vertex word list
        nq = []
        step = 1 # count beginWord step
        
        while wordList: #move to next layer when current distance is done.
            for n in range(len(vq)): # make sure all vertexes has been travelled.
                currentV= vq.pop()
                # print(currentV)
                
                #find each word ladder from current vertex from wordList
                n=0
                while n < len(wordList):
                    a = wordList[n]
                    if sum(currentV[j] != a[j] for j in range(len(a))) <= 1: #check if the word in wordList has only one character different from currentV.
                        # print('word ladder: ', a)
                        nq.insert(0,a)
                        # print(nq)
                        wordList.remove(a)
                    else: n+=1
                
            if endWord in nq:
                return step+1
            elif not nq: return 0
            else:          
                vq = nq
                nq=[]       
                step+=1
        return 0
# Dongdong's solution
# 58%
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        vq={}
        vq[beginWord] = None #current vertex word list
        nq = {}
        step = 1 # count beginWord step
        
        while vq: #move to next layer when current distance is done.
            if endWord in vq:
                return step
            subsearch = {}
            for i in range(len(beginWord)): # change vertex in vq as subsearch dictionary, which has removed index i character. In this case, we can match current target with wordList candidate which are masked as the same method.
                subsearch = {}
                for key in vq.keys():
                    subsearch[key[:i] + key[i+1:]] = None
                
                  #find each word ladder from current vertex from wordList
                n=0
                while n < len(wordList):
                    a = wordList[n]
                    if a[:i] +a[i+1:] in subsearch: #check if the word in wordList has only one character different from currentV.
                        nq[wordList.pop(n)] = None
                    else: n+=1
                
            vq = nq
            nq={}       
            step+=1
        return 0
        
