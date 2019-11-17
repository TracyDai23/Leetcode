class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1 for i in range(n)] for j in range(n)]
        total = n*n
        x,y=0,0
        i=1
        while i<=total:
            while y<n and res[x][y] <0:
                res[x][y] = i
                y += 1
                i += 1
            if i>total:
                break
            x+=1
            y-=1
            while x<n and res[x][y] <0:
                res[x][y] = i
                x += 1
                i += 1
            if i>total:
                break
            x-=1
            y-=1
            while y>=0 and res[x][y] <0:
                res[x][y] = i
                y -= 1
                i += 1
            if i>total:
                break
            y+=1
            x-=1
            while x>=0 and res[x][y] <0:
                res[x][y] = i
                x -= 1
                i += 1
            if i>total:
                break
            x+=1
            y+=1
        return res
