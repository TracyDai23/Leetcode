# Points: 
#1. data structure: set example {'a','.'}
#2. DFS: depth-first search, an algorithm from Graph portion.

# Solutions 1: Recursion

class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'} # {'a','.'} this is a set, not dictionary.

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

       
#Solution 2: Dynamic Programming (Following solution is in Python 2.7)
import unittest


class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()

# My own unfinished first attempt with 3 days efforts.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #standardize p: 1)"X*.*X*" ; 2) "a*a"; 3)".."; 
        # p=list(p)
        # for i in range(len(p)):
        #     if p[i:i+2]== '.*':
        #         print('i:',i)
        #         n=2
        #         while i+n+1 <len(p) and p[i+n+1] == "*":
        #             p=p[:i+2]+p[i+n+2:]
        #             n+=2
        #         n=2
        #         while i-n>=0 and p[i-n+1] == "*":
        #             p=p[i:]
        #             n+=2
        #     # print('p: ',p)
        #     elif len(p)>0 and p[i] =='*':
        #         n=1
        #         # while i+n <len(p)-1 and p[i-1] == p[i+n]:
        #         #     p=p[:i+n]+p[i+n+1:]
        #         #     # print(p[:i+n]+p[i+n+1])
        #         #     n+=1
        #         # if p[i-1] ==p[i+n]:
        #         #     p=p[:i+n]
        #     # elif p[i:i+1] == '..':
        #     #     n=1
        #     #     while i+n <len(p) and p[i]==p[i+n]:
        #     #         p=p[:i+1]+p[i+2:]
        #     #         n+=1
        # print(p)
        
        p=p[::-1] #reverse p
        s=s[::-1] #reverse s
        
        print(p, s)
        
        while len(s) >0:
            i=0 #index for p
            j=0 #index for s
            if p[i] != '.' and p[i]!= '*':
                if p[i]!=s[j]:
                    return False
                else:
                    p=p[1:]
                    s=s[1:]
            elif p[i] == '.':
                p=p[1:]
                s=s[1:]
            elif i>= len(p)-1 and p[i] =='*': #need to return False when * has no "." or character ahead. 
                print('* can not be the first of p')
                return False
            elif p[i] =='*':
                adv=p[i+1]
                if i+2<len(p) and adv == '.': # example: s = 'bbaaaaa', p='bb.*'
                    x=i+2
                    new_s=''
                    while x<=len(p)-1:
                        if p[x] == '*' or p[x]=='.':
                            break
                        else: 
                            new_s += p[x] 
                            x+=1
                    if new_s not in s:
                        print('substring check after .*')
                        return False
                    else:
                        s= s[x:]
                        # p=p[]
                elif adv=='.' and i+2 >= len(p):
                    return True
                elif adv =='*': #for p has "**" pattern, return False
                    print('** check')
                    return False
                else:
                    while len(s)>0 and s[j]==adv:
                        s=s[1:]
                    p=p[2:]
        if s!=p:
            print('general check')
            return False
                    
        return True  
                    
