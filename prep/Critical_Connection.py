class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for item in connections:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])

        edges = len(connections)
        visited = [False] * edges
        disc = [float('inf')] * edges
        low = [float('inf')] * edges
        parent = [-1] * edges
        self.appear = 0
        self.res = []


        def bridgeUtil(i,visited,parent,low,disc):
            visited[i] = True

            disc[i] = self.appear
            low[i] = self.appear
            self.appear += 1

            for j in graph[i]:
                if visited[j] == False:
                    parent[j] = i
                    bridgeUtil(j,visited,parent,low,disc)

                    low[i] = min(low[i],low[j])

                    if low[j] >disc[i]:
                        self.res.append(sorted([i,j]))
                elif j != parent[i]:
                    low[i] = min(low[i],disc[j])

        for i in range(edges):
            if visited[i] == False:                                 # if edge has not been visited. What is the visiting condition?
                bridgeUtil(i,visited,parent,low,disc)

        return self.res
