class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        #DFS转遍当前点的所有朋友圈
        #如果下一个点没被访问过，那就转这个点
        #row行col列是1，那就去检查col列
        
        
        visited = [0]*len(M)
        count = 0
        
        def dfs(row):
            
            for i in range(len(M)):
                if M[row][i] == 1 and visited[i]  ==0:
                    visited[i] =1
                    dfs(i)
                    
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(i)
                count+=1
                
        return count


        
