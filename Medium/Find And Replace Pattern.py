class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        b=pattern
        
        def func(a):
            return len(set(a))==len(set(b))==len(set(zip(a,b)))
        
        return filter(func,words)