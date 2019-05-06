#83.2% 
# Back-track # take away:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'1':['*'],'2':['a','b','c'], '3': ['d','e','f'],'4': ['g','h','i'], '5': ['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'], '8': ['t','u','v'],'9':['w','x','y','z'],'0':[' ']}

        os,ns,i,j=[],[],0,0
        for i in range(len(digits)):
            
            if i ==0:
                ns = d[digits[i]]
                # print(ns)
            else:
                os=ns
                ns=[]
                n=0
                while n<len(os):
                    a = os[n]
                    # print(a)
                    for j in range(len(d[digits[i]])):
                        ns.append(a+d[digits[i]][j])        
                        # print(ns)
                    n+=1
        return ns
            
# wrong answer的一版答案，没有理解到当赋值一个list 到另一个list， 然后对当前list.pop()的时候，另一个list也会被影响。因为赋值是复制的location，而不是value
# 解决方案是： os=ns.copy() #deepcopy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'1':['*'],'2':['a','b','c'], '3': ['d','e','f'],'4': ['g','h','i'], '5': ['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'], '8': ['t','u','v'],'9':['w','x','y','z'],'0':[' ']}

        os,ns,i,j=[],[],0,0
        for i in range(len(digits)):
            
            if i ==0:
                ns = d[digits[i]]
                # print(ns)
            else:
                os=ns
                ns=[]
                while os:
                    a = os.pop(0)
                    # print(a)
                    for j in range(len(d[digits[i]])):
                        ns.append(a+d[digits[i]][j])        
                        # print(ns)
        return ns
  
  
# Official back-tracking solution:
#Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

#Here is a backtrack function backtrack(combination, next_digits) which takes as arguments an ongoing letter combination and the next digits to check.

#If there is no more digits to check that means that the current combination is done.
#If there are still digits to check :
#Iterate over the letters mapping the next available digit.
#Append the current letter to the current combination combination = combination + letter.
#Proceed to check next digits : backtrack(combination + letter, next_digits[1:]).

def test(digits):
    phone = {'1':['*'],'2':['a','b','c'], '3': ['d','e','f'],'4': ['g','h','i'], '5': ['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'], '8': ['t','u','v'],'9':['w','x','y','z'],'0':[' ']}

    def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]: #for loop实现了loop 2 的所有letters 和loop3的所有letters
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
         
    output = []
    if digits:
        backtrack("", digits)
    return output
        

def main():
    s= '23'
    test(s)
    
main()
            
            
