class TimeMap:

    def __init__(self):
        self.dic=collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.dic[key],(timestamp*-1,value))

    def get(self, key: str, timestamp: int) -> str:
        res=""
        
        for values in self.dic[key]:
            if abs(values[0])<=timestamp:
                res=values[1]
                break
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)