class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(set)
        dist = [float('inf')] * n
        dist[0] = 0
        
        for i, j, w in edges:
            graph[i].add((j, w + 1))
            graph[j].add((i, w + 1))
            
        heap = [(0, 0)]

        while heap:
            min_dist, index = heappop(heap)
            for neigh, weight in graph[index]:
                new_dist = min_dist + weight
                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    heappush(heap, (new_dist, neigh)) 
                    
        ans = sum(dist[i] <= maxMoves for i in range(n))
        
        for i, j, w in edges:
            w1, w2 = maxMoves - dist[i], maxMoves - dist[j]
            ans += (max(0, w1) + max(0, w2))
            if w1 >= 0 and w2 >= 0: ans -= max(w1 + w2 - w, 0)
                
        return ans