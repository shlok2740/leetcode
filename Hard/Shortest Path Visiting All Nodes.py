class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q=[(i,1<<i) for i in range(len(graph))]
        visited=set()
        
        last=(1<<len(graph))-1
        steps=0
        
        while True:
            new_q=[]
            
            for node,state in q:
                if state==last:
                    return steps
                
                for v in graph[node]:
                    if (state | 1<<v , v) not in visited:
                        visited.add((state | 1<<v , v))
                        new_q.append((v , state | 1<<v))
                        
            q=new_q
            steps+=1
        