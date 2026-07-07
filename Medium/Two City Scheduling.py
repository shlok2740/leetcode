class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        cost = 0

        # First half → city A
        for i in range(n):
            cost += costs[i][0]

        # Second half → city B
        for i in range(n, 2 * n):
            cost += costs[i][1]

        return cost

