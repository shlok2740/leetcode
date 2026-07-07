class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        res=[]
        
        for i in range(n+1):
            res.append(factorial(n)//(factorial(i)*factorial(n-i)))
            
        return res