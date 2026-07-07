class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        words, w_to_p = s.split(' '), dict()
        
        if not len(p) == len(words): return False
        
        if not len(set(p)) == len(set(words)): return False # for the case `words=['dog', 'cat']` and  `p='aa'`
        
        for i in range(len(words)):
            if words[i] in w_to_p: 
                if not w_to_p[words[i]] == p[i]: return False
            else:
                w_to_p[words[i]] = p[i]
                
        return True