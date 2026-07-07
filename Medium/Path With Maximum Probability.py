class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph=collections.defaultdict(list)
        q=deque([start])
        
        for i,(a,b) in enumerate(edges):
            graph[a].append([b,i])
            graph[b].append([a,i])
            
        prob=[0.0]*n
        prob[start]=1.0
        
        while q:
            curr=q.popleft()
            
            for neighbour,i in graph.get(curr,[]):
                if prob[curr]*succProb[i]>prob[neighbour]:
                    prob[neighbour]=prob[curr]*succProb[i]
                    q.append(neighbour)
                    
        return prob[end]