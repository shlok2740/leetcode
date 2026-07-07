class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=[set() for _ in range(numCourses)]
        
        for pre,cur in prerequisites:
            graph[cur].add(pre)
        
        visited = [0] * numCourses
        
        def dfs(cur):
            if visited[cur]:
                return graph[cur]
            if not graph[cur]:
                return set()
            
            for i in set(graph[cur]):
                graph[cur] |= dfs(i)
                
            visited[cur]=1
            return graph[cur]
        
        for cur in range(numCourses):
            dfs(cur)
            
        return [pre in graph[cur] for pre,cur in queries] 