class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest=min(strs,key=len)
        for i,ch in enumerate(shortest):
            for st in strs:
                if st[i]!=ch:
                    return shortest[:i]
        return shortest