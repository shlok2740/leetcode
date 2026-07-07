class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        parent=[i for i in range(n)]
        
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            n1=find(x)
            n2=find(y)
            
            if n1==n2:
                return
            elif n1>n2:
                parent[n2]=n1
            else:
                parent[n1]=n2
                
        m1,m2={},{}
        
        for i in range(n):
            if stones[i][0] not in m1:
                m1[stones[i][0]]=i
            if stones[i][1] not in m2:
                m2[stones[i][1]]=i
        
        for i,stone in enumerate(stones):
            if m1[stone[0]] != i:
                union(i,m1[stone[0]])
            if m2[stone[1]] != i:
                union(i,m2[stone[1]])
                
        ans = 0
        for i in range(n):
            if parent[i] != i:
                ans+=1
                
        return ans