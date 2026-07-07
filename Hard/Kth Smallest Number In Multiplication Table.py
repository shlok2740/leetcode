class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def smallNumber(num):
            count=0
            for i in range(1,m+1):
                add=min(num//i,n)
                if add==0:
                    break
                count+=add
            return count>=k
        
        low,high=1,m*n
        while low<high:
            mid=low+((high-low)//2)
            
            if smallNumber(mid):
                high=mid
                
            else:
                low=mid+1
                
        return low