# Solution 1:  collections.Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for k in count:
            if count[k] ==1:
            return k

# Solution 2: Hash table use
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        htable = {}
        for i in nums:
            try:
                htable.pop(i)
            except:
                htable[i]=1
        return htable.popitem()[0]


# Solution 3:  XOR (^) operator and Reduce () function (import functools)
# Bitwise XOR sets the bits in the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.
# Example: 3^3 = 0; 0^0 =0; 1^2= 3
import functools 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, nums)
