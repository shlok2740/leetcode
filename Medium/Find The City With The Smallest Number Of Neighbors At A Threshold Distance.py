class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for i in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
            
        for i, j, w in edges:
            dist[i][j] = w
            dist[j][i] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])
                    
        res, min_count, min_distance = 0, float('inf'), [0] * n
        
        for i in range(n):
            min_distance[i] = sum([dist[i][j] <= distanceThreshold for j in range(n)])
            
            if min_count >= min_distance[i]:
                res = i
                min_count = min_distance[i]
                
        return res