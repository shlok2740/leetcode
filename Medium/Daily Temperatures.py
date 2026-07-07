class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                current=stack.pop()
                ans[current]=i-current
            stack.append(i)
            
        return ans