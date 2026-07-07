class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans=" "
        return ans.join(s.split()[:k])
        