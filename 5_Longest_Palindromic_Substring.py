# 83.37%
# Time complexity: O(N^2) because line 12 list in operation is an O(n) statement.

# Other's solution: Manacher algorithm
#http://en.wikipedia.org/wiki/Longest_palindromic_substring

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
        

# Other's solution:
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
