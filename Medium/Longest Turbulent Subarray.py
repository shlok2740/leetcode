class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_count,count=0,0
        
        for i in range(len(arr)):
            if i>=2 and (arr[i-2]<arr[i-1]>arr[i] or arr[i-2]>arr[i-1]<arr[i]):
                
                count+=1
                
            elif i>=1 and arr[i-1] != arr[i]:
                 
                count=2
                
            else:
                count=1
                
            max_count=max(max_count,count)
            
        return  max_count