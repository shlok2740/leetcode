class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        an={}
        
        for i in s:
            if i in an:
                an[i]+=1
            else:
                an[i]=1
                
        for i in t:
            if i in an:
                an[i]-=1
            else:
                an[i]=1
                
                
        for i in an:
            if an[i]>0:
                return False
            
        return True