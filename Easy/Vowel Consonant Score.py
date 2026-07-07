class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        ans,v,c = 0,0,0
        vowels = ["a","e","i","o","u"]

        for i in s:
            if i.isalpha() and i in vowels:
                v+=1
            elif i.isalpha() and i not in vowels:
                c+=1

        if c < 1:
            return 0

        ans = v//c

        return ans
        