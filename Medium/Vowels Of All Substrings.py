class Solution:
    def countVowels(self, word: str) -> int:
        return sum((i + 1) * (len(word) - i) for i, ch in enumerate(word) if ch in 'aeiou')