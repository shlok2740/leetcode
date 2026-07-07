class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        minimum = inf
        
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num*2)
                
        heapq.heapify(evens)
        min_deviation = inf
        
        while evens:
            val = -heapq.heappop(evens)
            min_deviation = min(min_deviation, val - minimum)
            
            if val % 2 == 0:
                minimum = min(minimum, val // 2)
                heapq.heappush(evens, -val // 2)
            else:
                break
                
        return min_deviation