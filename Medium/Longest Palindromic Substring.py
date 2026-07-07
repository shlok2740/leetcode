class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        
        def helper(i,j):
            while (i>=0 and j<len(s) and s[i]==s[j]):
                i-=1
                j+=1
            return s[i+1:j]
        
        for i in range(n):
            ans=max(helper(i,i),helper(i,i+1),ans,key=len)
            
        return ans