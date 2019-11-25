#Time: O(MN) 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ext = set()
        h = len(grid)
        w = len(grid[0])
        cnt = 0

        def dfs(i, j): # recursion
            
            if i>h-1 or i<0 or j >w-1 or j<0 or grid[i][j] == '0' or (i,j) in ext:
                return
            else:
                ext.add((i,j))
            for d in directions:
                dfs(i+d[0], j+d[1])
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and (i,j) not in ext:
                    cnt+=1
                    dfs(i, j)
                    
        return cnt
