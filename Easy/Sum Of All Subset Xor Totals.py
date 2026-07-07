class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        def go(i = 0, x = 0):
            if i == len(A):
                return x
            include = go(i + 1, x ^ A[i])  # ✅ case 1: include
            exclude = go(i + 1, x)         # \U0001f6ab case 2: exclude
            return include + exclude
        return go()