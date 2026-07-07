class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        max_val=0
        
        hashmap={0:-1}
        
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            if nums[i]==1:
                count+=1
                
            
            if count in hashmap:
                max_val=max(max_val,i-hashmap[count])
            else:
                hashmap[count]=i
                
        return max_val