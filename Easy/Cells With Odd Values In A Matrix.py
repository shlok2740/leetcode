class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        x,y = [0]*n,[0]*m
        #print(x)
        #print(y)
        for r,c in indices:
            x[r] += 1
            y[c] += 1
        #print(indices)
        #print(x)
        #print(y)
        return sum([ (r+c)%2 for c in y for r in x])  