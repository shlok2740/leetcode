class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(x) for x in words if not Counter(x)-Counter(chars))