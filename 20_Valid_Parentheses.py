# Resolved 85.57%
# stack pop()

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 ==1:
            return False
        a=['(','[','{']
        st=[]
        for i in range(len(s)):
            if s[i] in a:
                st.append(s[i])
            else:
                try:
                    p=st.pop()
                except:
                    return False # when start with back brackets
                else:
                    if p=='(' and s[i] ==')':
                        continue
                    elif p=='[' and s[i] ==']':
                        continue
                    elif p=='{' and s[i] =='}':
                        continue
                    else:
                        return False # when brackets type did not match
        if len(st)>0: # when pair did not match
            return False
        else:
            return True
