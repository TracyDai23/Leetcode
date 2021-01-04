# 变种的200. 我没有做出来，思路是对的，用相对位置来记录island形状，但是没有implement出来，因为过于急躁，没有能够把思路整理清楚再修改。
# 这题的难点是把开始位置default成（0，0），这样直接完成位置记录，而不需要像我考虑的，是把所有绝对位置都拿到之后再计算相对位置。
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shape = set()
        h = len(grid)
        w = len(grid[0])
        
        def helper(p, positions, rel_pos):
            a, b = p            
            grid[a][b] = -1 #这个直接改数字实际上就是省略了visited的步骤
            
            for d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                x = a+d[0]
                y = b+d[1]
                if (0<=x<h and 0<=y<w and grid[x][y] ==1 ):
                    new_rel_pos = (rel_pos[0]+d[0], rel_pos[1]+d[1])
                    positions.append(new_rel_pos)
                    helper((x, y), positions, new_rel_pos)
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] ==1:
                    positions = []
                    helper((i,j), positions, (0,0))
                    print(positions)
                    shape.add(tuple(positions))
        
        return len(shape)
                    
                    
