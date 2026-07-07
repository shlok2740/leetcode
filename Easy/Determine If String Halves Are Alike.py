class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vs, n = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], len(s)//2
        a, b = Counter(s[:n]), Counter(s[n:])
        return sum(a[v] for v in vs) == sum(b[v] for v in vs)