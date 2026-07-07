class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        mid=len(nums)//2
        
        left=self.sortArray(nums[0:mid])
        right=self.sortArray(nums[mid:])
        
        def merge(arr1,arr2):
            result=[]
            point1,point2=0,0
            while point1<len(arr1) and point2<len(arr2):
                if arr1[point1]<arr2[point2]:
                    result.append(arr1[point1])
                    point1+=1
                else:
                    result.append(arr2[point2])
                    point2+=1
                    
            
            result.extend(arr1[point1:])
            result.extend(arr2[point2:])
                    
            return result
        
        return merge(left,right)