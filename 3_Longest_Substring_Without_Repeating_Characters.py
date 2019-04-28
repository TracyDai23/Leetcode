# 52.52%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lmax = 0 #track longest non-repeating substring length
        # l = 0
        subst = [] #hold substring characters in a list
        
        for i in range(len(s)):
            if s[i] in subst:
                idx = subst.index(s[i])
                subst = subst[idx+1:]
                subst.append(s[i])
                lmax = max(lmax,len(subst))
                # print(subst)
            else:
                subst.append(s[i])
                # print(subst)
                lmax = max(lmax,len(subst))

        return lmax
        
# Other's solution: 99%
# dictionary to save character position index. 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = lmax = 0 #track longest non-repeating substring length
        # l = 0
        usedchar = {} #hold substring characters in a dictionary
        
        for i in range(len(s)):
            if s[i] in usedchar and start <= usedchar[s[i]]:
                start = usedchar[s[i]]+1
            else:
                lmax = max(lmax, i-start+1)
            
            usedchar[s[i]] = i
        return lmax
        
