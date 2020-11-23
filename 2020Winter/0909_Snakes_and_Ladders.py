# My first trial, still need to debug.
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        odd_dirct = 1
        even_dirct = -1
        if len(board)%2 == 0:
            odd_dirct = -1
            even_dirct = 1
            
        myDict = {} #key: number, value:(x,y)
        myPDict = {} # key: (x,y), value: number
        N = len(board)
        n =  N * N
        for i in range(len(board)):
            dirct = 0
            if i%2 ==0:
                dirct = even_dirct
            else: dirct = odd_dirct
            if dirct == -1:
                j= N-1
                while j>=0:
                    myDict[n] = (i, j)
                    myPDict[(i,j)] = n
                    n-=1
                    j-=1
            else:
                j = 0
                while j< N:
                    myDict[n] = (i, j)
                    myPDict[(i,j)] = n
                    n-=1
                    j+=1
        print(myDict)
        
#         def findNextPosition(i, j):
#             dirct = 0
#             if i%2 ==0:
#                 dirct = even_dirct
#             else: dirct = odd_dirct
#             if  (j <=0 and dirct ==-1) or (j >=N-1 and dirct == 1):
#                 i-=1
#                 return (i, j)
#             else:
#                 j=j +1*dirct
#                 if board[i][j] != -1:
#                         v =board[i][j]
#                         i = myDict[v][0] 
#                         j = myDict[v][1]
#                         print("slide to another location: ", i, ', ', j, "new board value: ", v)
#                 return (i, j)
                
        
        # Step2: 开始挪位置从（N-1，0）开始
        q = collections.deque()
        q.append((N-1, 0))
        level = 0
        visited = set()
        while q:
            print(q, "tmp: ", q[0])
            level +=1
            l = collections.deque()
            for k in range(len(q)):
                tmp = q.popleft()
                i, j = tmp[0], tmp[1]

                if (i== 0 and j == 0): #myDict[N*N]:
                    print("hit")
                    return level
                v = myPDict[(i, j)]
                for m in range(1, 7):
                    nv = v+m
                    x, y = myDict[nv]
                    if x>=0 and x <N and y>=0 and y<N and (x, y) not in visited:
                        if board[x][y] != -1:
                            nv =board[x][y]
                            x = myDict[nv][0] 
                            y = myDict[nv][1]
                            l.append((x, y))
                            visited.add((x,y))
                            print("slide to another location: ", x, ', ', y, "new board value: ", nv)

                        elif (x, y) not in visited:
                            l.append((x,y))
                            visited.add((x, y))
            
            q = l
                

                
                        
                
        
                    
            
            
            
            
