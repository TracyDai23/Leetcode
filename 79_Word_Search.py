class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w,h = len(board[0]),len(board)
        res = False
        c, substring, p = word[0], word[1:], [0,0]
               
        
        def bt(c, substring, p,visited):
            print(c, substring, p,visited)
            
            
            if not substring:
                return True
            #check up
            if p[1]>0 and p not in visited:
                bt(c,substring,[p[0]-1,p[1]],visited)

            #check down
            if p[1]< h and (p not in visited):
                bt(c,substring,[p[0]+1,p[1]],visited)

            #check left
            if p[0]>0 and (p not in visited):
                bt(c,substring,[p[0],p[1]-1],visited)

            #check right
            if p[0]<w and (p not in visited):
                bt(c,substring,[p[0],p[1]+1],visited)
            
            if c == board[p[0]][p[1]]:
                visited = []
                bt(substring[0],substring[1:], p,visited)
            else:
                visited.append(p)
                
            
            
                
            
        
        #main portion:
        for j in range(w):
            for i in range(h):
                if c == board[i][j]:
                    p = [i,j]
                    visited = []
                    print(p)
                    bt(substring[0],substring[1:],p, visited)
                else:
                    continue
                
                
                
                
        return res
