class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i,j,n=0,0,len(s)
        res=[]
        
        while i<n:
            while j<n and s[j]==s[i]:j+=1
            
            if (j-i)>2:res.append([i,j-1])
                
            i=j
            
        return res