class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {l:i for i,l in enumerate(list1)}
        sm = {l:i+d[l] for i,l in enumerate(list2) if l in d}
        mn = min(v for v in sm.values())
        return [k for k,v in sm.items() if v == mn]