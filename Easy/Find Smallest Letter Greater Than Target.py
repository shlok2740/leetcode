class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1]<=target:
            return letters[0]
        for letter in letters:
            if letter>target:
                return letter