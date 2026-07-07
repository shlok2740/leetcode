class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = [[float(inf), point[0], point[1]] for point in points]
        graph[0][0], cost = 0, 0
        while graph:
            dist, x, y = heapq.heappop(graph)
            cost += dist
            for nei in graph:
                d, nx, ny = nei
                edge = abs(x-nx) + abs(y-ny)
                if edge < d:
                    nei[0] = edge
            heapq.heapify(graph)
        return cost