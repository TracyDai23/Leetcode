

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=list(str(x))
        for i in range(len(x)):
            y=i*(-1)
            print('x[i], x[-i]:', x[i],x[y], x[-1])
            if x[i] != x[-i]:
                return False
            
        return True
