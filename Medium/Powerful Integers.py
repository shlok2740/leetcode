class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xi={x**i for i in range(20) if x**i <=bound}
        yj={y**j for j in range(20) if y**j <=bound}
        
        return list({i+j for i in xi for j in yj if i+j<=bound})