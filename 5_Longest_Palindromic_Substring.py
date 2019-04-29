# 83.37%
# Time complexity: O(N^2) because line 12 list in operation is an O(n) statement.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sv= s[::-1]
        sb = []
        start = lmax = 0
        
        i=0
        while i <len(s)+1: # Was using for loop, but will ignore character. While loop is better.
            if s[start:i] in sv:
                # Added and s[start:i] == s[start:i][::-1] after a wrong case 'accdefcaa'
                if lmax <= i-start and s[start:i] == s[start:i][::-1]:
                    sb = s[start:i]
                    # print(start, i, s[start:i])
                    lmax = i-start
                i+=1
            else:
                start = start+1
                i=start
        return sb
        
