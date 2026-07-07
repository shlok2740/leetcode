class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=collections.defaultdict(dict)
        
        for (num,den),val in zip(equations,values):
            graph[num][num]=graph[den][den]=1.0
            graph[num][den]=val
            graph[den][num]=1/val
            
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j]=graph[i][k]*graph[k][j]
        
        return [graph[num].get(den,-1.0) for num,den in queries]