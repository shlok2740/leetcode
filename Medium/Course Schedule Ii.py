class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq={ c : [] for c in range(numCourses)}
        
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
            
        output=[]
        visited=set()
        iscycle=set()
        
        
        def dfs(crs):
            if crs in iscycle:
                return False
            if crs in visited:
                return True
            
            iscycle.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
                
            iscycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return output