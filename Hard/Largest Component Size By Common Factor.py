class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        arr = {i:i for i in nums}
        sz = {i:1 for i in nums}
        
        def find(x):
            if x != arr[x]:
                arr[x] = find(arr[x])
            return arr[x]
        
         
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return
            if x > y: x, y = y, x
            sz[x] += sz[y]
            arr[y] = arr[x]
            
        nmax = max(nums)+1
        snum = set(nums)
        isprime = [True] * nmax
        for i in range(2, nmax):
            if not isprime[i]:continue
            last = None
            for j in range(i, nmax, i):
                isprime[j] = False
                if j in snum:
                    if last == None: 
                        last = j
                    else:
                        union(last, j)
        return max(sz.values())