class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        
        heap=[]
        max_time=0
        
        for time,end_time in courses:
            heappush(heap,-time)
            max_time += time
            
            if max_time > end_time:
                big_time = heappop(heap)
                max_time += big_time
                
        return len(heap)