class Solution:
    def minimumSum(self, num: int) -> int:
        stack=[]

        while num>=1:
            stack.append(num%10)
            num//=10

        stack.sort()

        return 10*(stack[0]+stack[1])+(stack[-1]+stack[-2])