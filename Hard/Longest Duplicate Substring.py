class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ret=''
        j=1
        for i in range(len(s)):
            
            while s[i:i+j] in s[i+1:]:
                ret=s[i:i+j]
                j+=1
                
        return ret