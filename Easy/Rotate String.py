class Solution:
    def rotate(self, s: str) -> str:
        first_char = s[0]
        
        s2 = s[1:]
        
        s2 += first_char
        
        return s2
    
    
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            s = self.rotate(s)
            if s == goal:
                return True
            
        return False