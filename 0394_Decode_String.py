class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for c in s:
            print("c: " , c)
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0 #这里很聪明的完成了后续的数字的更新，这样如果数字是两位数可以处理好，同时不会把之前的数据带到下一轮
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
                print("curString: ", curString, ", prevString: ", prevString)
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
            print("stack: ", stack)
            print("curString: ", curString, "curNumber: " ,curNum)
        return curString
        

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
                            
                        
                        
