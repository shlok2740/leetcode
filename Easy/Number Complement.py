class Solution:
    def findComplement(self, num: int) -> int:
        mask = num
        
        for i in [1,2,4,8,16]:
            mask |= mask>>i
        
        return mask ^ num