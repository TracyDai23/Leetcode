class Solution:
    def __init__(self):
        self.memo = {}
    
    def recursive_with_memo(self, index, s):
        # Base case: when scan to the end of string S, return 1. Meaning successfully reached a possible solution.
        if index ==len(s):
            return 1
        
        if s[index] == "0": return 0
        
        if index == len(s)-1:
            return 1
        
        # memoization is needed since we might encounter the same sub-string.
        if index in self.memo:
            return self.memo[index]
        # Main calculation part
        ans = self.recursive_with_memo(index+1, s) \
                + (self.recursive_with_memo(index+2, s) if (int(s[index: index+2]) <=26) else 0)
        
        # Save for memoization
        self.memo[index] = ans
        
        return ans
    
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        return self.recursive_with_memo(0, s)
        
        
        
        
