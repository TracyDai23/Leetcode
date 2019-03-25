# First try accepted. 66%
# Dynamic Programming
# Time complexity: O(N), Space complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        numWays = {0:0, 1:1, 2:2}
        steps = [1,2]
        for i in range(3,n+1):
            numWays[i] = numWays[i-1]+numWays[i-2]
        return numWays[n]
        
'''这道题作为DP的启蒙题(拥有非常明显的重叠子结构)
Top-Down

这道题自顶向下的思考：如果要爬到n台阶，有两种可能性:

    在n-1的台阶处爬一层台阶
    在n-2的台阶处爬两层台阶

继续向下延伸思考，到达每一次层一共有几种方法这个问题就变成了2个子问题：

    到达n-1层台阶有几种方法
    到达n-2层台阶有几种方法

之后对返回子问题之和即可。 
Recursion:
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


Recursion TLE原因：

以上代码实现之所以会TLE，是因为递归的时候出现了很多次重复的运算。就如上图显示的爬n-2层的计算出现了2次，这种重复计算随着input的增大，会出现的越来越多，时间复杂度也会将以指数的级别上升。

优化思路：

这时候的思路为：如果能够将之前的计算好了的结果存起来，之后如果遇到重复计算直接调用结果，效率将会从之前的指数时间复杂度，变成O(N)的时间复杂度。

实现方法：

有了思路，实现方面则开辟一个长度为N的数组，将其中的值全部赋值成-1，具体为什么要用-1，是因为这一类问题一般都会要你求多少种可能，在现实生活中，基本不会要你去求负数种可能，所以这里-1可以成为一个很好的递归条件/出口。
然后只要我们的数组任然满足arr[n] == -1，说明我们在n层的数没有被更新，换句话说就是我们还在向下递归或者等待返回值的过程中，所以我们继续递归直到n-1和n-2的值返回上来。这里注意我们递归的底层，也就是arr[0]和arr[1]，我们要对起始条件进行初始化：arr[0], arr[1] = 1, 2

'''
