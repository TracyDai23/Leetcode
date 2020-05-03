## Sliding Window question

# Two Dequeue Solution:
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        A = nums
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            # print(a, maxd, mind)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i
# Two Heap Solution
 def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res

# My Attempt codes in contest:

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dp = [null]*len(nums)
        level = 2
        res = 1 #at least number will be the same comparing to itself.
        #initialize dp
        for i in len(nums):
            if i<level-1:
                dp[i] = 0
            else:
                dp[i] = nums[i] - nums[i-1] 
        print(dp)
        dpmin = abs(dp[0])
        for j in dp：
            if dpmin < abs(j):
                dpmin = abs(j)
        if dpmin <= limit:
            res =2
                
        # check different level
        move_nums = nums
        while level <len(move_nums):
            for i in len(nums):
            if i<level-1:
                dp[i] = 0
            else:
                dp[i] = dp[i] + dp[i-1] 
            print(dp)
