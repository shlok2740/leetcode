class DSU:
    def __init__(self,n):
        self.child=[i for i in range(n)]
        self.size=[1]*n
        
    def find(self,x):
        if self.child[x]!=x:
            self.child[x]=self.find(self.child[x])
        return self.child[x]
    
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        
        if x==y:
            return
        
        if self.size[x]>self.size[y]:
            x,y=y,x
            
        self.child[x]=y
        self.size[y]+=self.size[x]
        
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        email_to_name={}
        dsu=DSU(n)
        
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_name:
                    email_to_name[email]=i
                else:
                    dsu.union(i,email_to_name[email])
                    
        components=defaultdict(set)
        
        for email in email_to_name.keys():
            components[dsu.find(email_to_name[email])].add(email)
            
            
        ans=[]
        for keys,values in components.items():
            ans.append([accounts[keys][0]]+sorted(list(values)))
            
        return ans