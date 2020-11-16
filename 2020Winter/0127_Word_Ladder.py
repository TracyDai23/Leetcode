[BFS] Learnt from Solution, and coded myself.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0
        
        L = len(beginWord)
        patternMap = collections.defaultdict(list)
        # start by creating patternMap {"pKey": [all qualified words in wordList]} example: {"*ot": ["hot","dot","lot"]}
        for i in range(L):
            for w in wordList:
                patternMap[w[:i] +"*"+w[i+1:]].append(w)
        # print(patternMap)
        
        # start BFS search of levels 
        visited = {beginWord}
        stk = collections.deque([beginWord])
        level = 1
        
        while stk: # loop to check all elements resolved. 
            level+=1
            # cur = stk.popleft()
            for i in range(len(stk)): #loop all qualified words that are parallel, like [dot, lot]
                cur = stk.popleft()
                for j in range(L): # loop to check pattern: *ot, h*t, ho*
                    p = (cur[:j]+"*"+cur[j+1:])
                    # print(cur,p, patternMap[p])
                    for w in patternMap[p]: # loop to check if any end word in pattern p. 
                        # print(w, stk)
                        if w == endWord:
                            return level
                        if w not in visited:
                            visited.add(w)
                            stk.append(w)
        return 0
                
