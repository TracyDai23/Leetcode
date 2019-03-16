# Points:
# 1. enumerate function provide (index, value) from n-array or list.

#Optimized solution:
# This method will pull value as key and XY as pair in XY_set. And then check the set if any existing value in 1)the same row
#, 2) the same colume, 3) or the same 3*3 cube.


class Solution:
    def isValidSudoku(self, board):
        XY_set ={}
        for (i,row) in enumerate(board):
            for (j,item) in enumerate(row):
                if item !='.':
                    if item not in XY_set:
                        XY_set[item] =[[i,j]]
                    else:
                        temp_set = XY_set[item]
                        if i in [ele[0] for ele in temp_set]: # Not fully understand this for loop 
                            return False
                        if j in [ele[1] for ele in temp_set]:
                            return False
                        for ele in temp_set: 
                            if ele[0]//3 == i//3 and ele[1]//3== j//3:
                                return False
                        XY_set[item] += [[i,j]]
        return True

# 1st Try:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            print (board[i])
        
        ifValid = True
        for x in range(9):
            htable ={}
            h1table={}
            for y in range(9):
                if board[x][y] != "." and ifValid:
                    
                    try: 
                        htable.pop(board[x][y])
                    except: 
                        htable[board[x][y]] =1
                    else: 
                        print('row check')
                        ifValid = False
                
                if board[y][x] != "."and ifValid:                    
                    try: 
                        h1table.pop(board[y][x])
                    except: 
                        h1table[board[y][x]] =1                        
                    else:
                        print('column check')
                        ifValid = False
                        
        for x in range(0,9,3):
            for y in range(0,9,3):
                h2table = {}
                i = x//3
                j = y//3
                a,b=x,y
                while a//3==i and ifValid:
                    b=y
                    while b//3==j and ifValid:
                        print("a, b, i,j",a,b,i,j)
                        if board[a][b] != "." and ifValid:
                            try: 
                                h2table.pop(board[a][b])
                            except: 
                                h2table[board[a][b]] =1
                            else: 
                                print(h2table)
                                print('3_3 check',a,b)
                                ifValid = False
                        b+=1
                    a+=1
                print("Move to next loop: a, b", a, b)
                    
                    
                
        return ifValid
