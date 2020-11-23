class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        myDict = {}
        a = 'a'
        for i in range(26):
            myDict[i+1] = chr(ord(a)+i)
            # print(myDict)
        # 思路： 前面全是a， 后面全是z，只有中间有且只有一个位置可以是其他字母
        # Step 1: 找到所有应该填z的：
        i = 26
        z = (k-n+1)//i
        while k-z*i > n-z-1+i:
            z+=1
        if z >0:
            for j in range(z):
                res+=myDict[i]
                k-=i
        # 找到中间位置应该的value
        left = k - (n-z-1)
        res+=myDict[left]
        
        #把剩下的都填上a
        for j in range(n-len(res)): 
            res+='a'
        
        return res[::-1]
        
        
