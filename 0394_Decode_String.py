# incorrect first try
class Solution:
    def decodeString(self, s: str) -> str:
        # recusion is to have base case and reoccuring scenario
        if not s:
            return ""
        
        cstack = []
        res =[]
        
        def dfs(s, i):
            if not s:
                return ""
            tmp ="" # this will be repeating string holder at current layer.
            #base case:
            for i in range(i, len(s)):
                print("s: ", s, "i: ", i)
                if s[i] == "]":
                    c = cstack.pop()
                    for j in range(c): 
                        res.append(tmp.pop())
                    return
                if s[i].isalpha():
                    tmp = tmp +s[i]
                elif s[i].isnumeric():
                    num = ""
                    while i<len(s):
                        if s[i].isnumeric():
                            num= num+(s[i])
                        else:
                            stack.append(int(num))
                            print(stack)
                            break
                    i-=1
                elif s[i] == '[':
                    dfs(s, i)
        
        dfs(s, 0)
        return res
                            
                        
                        
