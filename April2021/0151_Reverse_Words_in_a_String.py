class Solution:
    def reverseWords(self, s: str) -> str:
        s = " " + s.strip()
        p1 = 0
        p2 = len(s)-1
        
        while p2>=p1:
            if s[p2].isspace():
                tmp = s[(p2+1):].strip()
                print(tmp)
                if tmp:          
                    s = s[:p1] +" " + tmp + s[p1:p2]
                    l = len(tmp) +1
                    p1 +=l
                    p2 +=l
            p2-=1
                
        return s[1:]
                
                
