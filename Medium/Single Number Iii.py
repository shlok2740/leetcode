class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for n in nums:
            xor ^= n
            
        first_bit= xor & (xor-1)  ^ xor
        num1=0
        
        for n in nums:
            if n & first_bit:
                num1^=n
                
        return [num1,num1^xor]