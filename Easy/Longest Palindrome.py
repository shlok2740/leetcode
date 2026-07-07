class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen=set()
        for c in s:
            if c in seen:
                seen.remove(c)
            else:
                seen.add(c)
                
        return 1+len(s)-len(seen) if len(seen)>0 else len(s)