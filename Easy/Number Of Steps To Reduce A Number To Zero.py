class Solution:
    def numberOfSteps(self, num: int) -> int:
        bit=bin(num)[2:]
        return len(bit)-1+bit.count('1')