class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents={}
        
        for eq in equations:
            if eq[1]=='=':
                self.union(parents,eq[0],eq[3])
        for eq in equations:
            if eq[1]=="!":
                if self.find(parents,eq[0])==self.find(parents,eq[3]):
                    return False
                
        return True
    
    def union(self,parents,var1,var2):
        if var1 not in parents:
            parents[var1]=var1
            
        if var2 not in parents:
            parents[var2]=var2
            
        find1=self.find(parents,var1)
        find2=self.find(parents,var2)
        
        if find1 != find2:
            parents[find1] = find2
            
            
    def find(self,parents,var):
        if var not in parents:
            parents[var]=var
            
        if parents[var]!=var:
            parents[var]=self.find(parents,parents[var])
            
        return parents[var]