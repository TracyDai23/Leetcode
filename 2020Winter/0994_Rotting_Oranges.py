#My wrong answer first try:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        aVisited = set()
        res = float("inf")
        
        # corner case: [[0,2,2]]
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = True
        if not flag:
            return 0
        
        # Main part:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # BFS to find min number of minutes
                    q = collections.deque([[(i,j)]])
                    level = 0
                    visited = {(i,j)}
                    # print(q, visited)
                    while q and q[0]: #每一层的list
                        l = []
                        tmp = q.popleft()
                        # print("step2: ", tmp, level)
                        for i in range(len(tmp)): #[(0,1),(1,0)]
                            #go thru 4 directions:
                            # print(i, tmp[i])
                            p=tmp[i]
                            if ((p[0]+1)<len(grid) and grid[(p[0]+1)][p[1]] == 0)\
                            and( p[0]-1>=0 and grid[p[0]-1][p[1]] == 0 )\
                            and( p[1]+1<len(grid[0]) and grid[p[0]][p[1]+1] == 0)\
                            and( p[1]-1>=0 and grid[p[0]][p[1]-1] == 0):
                                level-=1
                            if (p[0]+1)<len(grid) and grid[(p[0]+1)][p[1]] != 0 and (p[0]+1,p[1]) not in visited:
                                visited.add((p[0]+1,p[1]))
                                l.append((p[0]+1,p[1]))
                            if p[0]-1>=0 and grid[p[0]-1][p[1]] != 0 and (p[0]-1,p[1]) not in visited:
                                visited.add((p[0]-1,p[1]))
                                l.append((p[0]-1,p[1]))
                            if p[1]+1<len(grid[0]) and grid[p[0]][p[1]+1] != 0 and (p[0],p[1]+1) not in visited:
                                visited.add((p[0],p[1]+1))
                                l.append((p[0],p[1]+1))
                            if p[1]-1>=0 and grid[p[0]][p[1]-1] != 0 and (p[0],p[1]-1) not in visited:
                                visited.add((p[0],p[1]-1))
                                l.append((p[0],p[1]-1))
                        level+=1
                        q.append(l)
                        print(q,level)
                        aVisited.update(visited)
                    res = min(res, level-1)
        
        # check if any left over fresh orange did not rot
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in aVisited and grid[i][j] == 1:
                    return -1
        if res == float("inf"): return 0
        return res
        
                
                    
                        
                                
                            
                    
