class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.array=collections.defaultdict(list)
        
        for i,x in enumerate(arr):
            self.array[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.array[value],right)-bisect_left(self.array[value],left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)