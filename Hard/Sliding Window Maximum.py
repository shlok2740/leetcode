class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        index=collections.deque()
        l=r=0
        
        while r<len(nums):
            
            while index and nums[index[-1]]<nums[r]:
                index.pop()
            index.append(r)
                
            if l>index[0]:
                index.popleft()
                
            if (r+1)>=k:
                output.append(nums[index[0]])
                l+=1
                
            r+=1
            
        return output