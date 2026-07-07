class Solution:

    def __init__(self, w: List[int]):
        self.arr=[]
        s=sum(w)
        x=0
        for i in w:
            x+=i/s
            self.arr.append(x)

    def pickIndex(self) -> int:
        x = random.random()
        return bisect.bisect(self.arr, x)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()