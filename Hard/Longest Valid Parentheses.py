class Solution:
    def longestValidParentheses(self, s: str) -> int:
        index=[-1]
        res=0
        for i in range(len(s)):
            if s[i]=="(":
                index.append(i)
            else:
                index.pop()
                if len(index)==0:
                    index.append(i)
                else:
                    res=max(res,i-index[-1])
                    
        return res