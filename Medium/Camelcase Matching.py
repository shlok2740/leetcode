class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def pat(p,q):
            i=0
            for j,c in enumerate(q):
                if i<len(p) and p[i]==c:
                    i+=1
                elif c.isupper():
                    return False
                
            return i==len(p)
        
        return [pat(pattern,q) for q in queries]