class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        def dfs(i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return 0
            # elif grid[i][j] == 1: # 不需要这个条件了，因为grid[i][j] == 0 已经在上一步考虑了。+1 就在return的步骤完成了
            #     tmpm +=1
            visited.add((i, j))
            return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i,j+1) + dfs(i, j-1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    tmpm = dfs(i, j)
                    res = max(tmpm, res)
        
        return res
