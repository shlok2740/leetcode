class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary={x:-1 for x in nums1}
        
        stack=[]
        
        for n in nums2:
            while stack and stack[-1]<n:
                dictionary[stack.pop()] = n
            
            stack.append(n)
            
        return [dictionary.get(x,-1) for x in nums1]