class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter=0
        for ct in t:
            letter ^= ord(ct)
        for cs in s:
            letter ^= ord(cs)
            
        return chr(letter)