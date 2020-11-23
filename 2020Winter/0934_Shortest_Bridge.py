# 自己做出来的bfs
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # Step 1: find all edge nodes and save into queue
        q = collections.deque()
        lq = collections.deque()
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and len(lq) ==0:
                    q.append([i,j])
                    lq.append([i,j])
                    visited.add((i,j))
                    # print(lq,visited)
                    while q:
                        tmp = q.popleft()
                        i,j = tmp[0], tmp[1]
                        for dx, dy in dirs:
                            x, y = i+dx, j+dy 
                            if x<0 or y<0 or x>=len(A) or y>= len(A[0]):
                                continue
                            if A[x][y] == 1 and (x,y) not in visited:
                                q.append([x,y])
                                lq.append([x,y])
                                visited.add((x,y))
                                # print(lq,visited)
                # else:continue                                            
        # print(lq,visited)
        
        # Step 2: BFS to find shortest bridge
        level = 0
        while lq:
            level +=1
            for _ in range(len(lq)):
                tmp = lq.popleft()
                i,j = tmp[0], tmp[1]
                for dx, dy in dirs:
                    x, y =  i+dx, j+dy 
                    if x<0 or y<0 or x>=len(A) or y>= len(A[0]):
                        continue
                    if A[x][y] == 1 and (x,y) not in visited:
                        return level-1
                    elif (x,y) not in visited:
                        lq.append([x,y])
                        visited.add((x,y))
            
                        
                        
                
                
                
                
            
