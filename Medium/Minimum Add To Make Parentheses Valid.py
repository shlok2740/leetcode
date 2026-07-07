class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append("(") # stack top index + 1
            elif not stack: # stack top index < 0
                count += 1
            elif c == ")" and stack[-1] == "(":
                stack.pop() # stack top index - 1
        return count + len(stack)