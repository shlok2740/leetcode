class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)
        
        
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf=UnionFind(len(source))
        
        for x,y in allowedSwaps:
            uf.union(x,y)
        
        m=defaultdict(set)
        
        for i in range(len(source)):
            m[uf.find(i)].add(i)
        
        ans=0
        
        for indices in m.values():
            sourcecnt=Counter([source[i] for i in indices])
            targetcnt=Counter([target[i] for i in indices])
            
            diff=sourcecnt-targetcnt
            ans+=sum(diff.values())
        
        return ans