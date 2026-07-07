class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = list(s)
        for i in spaces:
            arr[i] = " "+arr[i]
        return ''.join(arr)