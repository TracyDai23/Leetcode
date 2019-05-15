# Other's solution
# Backtracking
# 逻辑： 1）基本情况： 字符长度等于两倍n就完成了字符串； 2）左括号数量等于n，右括号数量应该永远小于等于当前左括号； 3)在每一个分节点，需要解决的都是同一个问题：是不是可以加左括号和右括号


'''
                        (
            ((                     ()
    (((             (()           ()(
 ((()))       (()(      (())    ()()    ()((
              (()()     (())(   ()()()  ()(())
              (()())    (())()

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def trec(s='',left=0,right=0):
            if len(s) == 2*n:
                output.append(s)
                print(output)
                return
            if left<n:
                trec(s+'(',left+1,right)
            if right <left:
                trec(s+')',left, right+1)
        trec()
        return output
        
# My own try with Wrong Answer:
# 这个答案的问题是产生括号的逻辑没有理顺，条件分解不成功。 核心原因是对于recursion的理解不到位。
# recursion的核心原则是：1) 递归算法必须具有基本情况; 2)递归算法必须改变其状态并向基本情况靠近 3) 递归算法必须以递归方式调用自身。
# 实际构建的时候，要满足每一个树节点上是要做相同的判断。


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def trec(s,n):
            if not n:
                output.append(s)
                # print(output)
            else:
                n-=1
                trec('()'+s,n)
                trec(s+'()',n)
                trec('('+s+')',n)

        trec('',n)
        return list(set(output))
