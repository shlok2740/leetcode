class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d={}
        for ch in word1:
            d[ch]=d.get(ch,0)+1
        for ch in word2:
            d[ch]=d.get(ch,0)-1
        difFreq=max(abs(val) for val in d.values())
        return difFreq<=3