class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val=-1
        for i in range(len(arr)-1,-1,-1):
            arr[i],max_val=max_val,max(max_val,arr[i])
            
        return arr