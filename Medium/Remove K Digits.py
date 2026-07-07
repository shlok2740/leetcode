class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i,n=0,len(num)
        
        stack=[]
        
        if k>=n:
            return "0"
        
        while i<n:
            while k>0 and stack and int(stack[-1])>int(num[i]):
                stack.pop()
                k-=1
            stack.append(num[i])
            i+=1
            
        while k>0:
            stack.pop()
            k-=1
            
        return str(int(''.join(stack)))