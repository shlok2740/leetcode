class Solution:
    def calculate(self, s: str) -> int:
        
        stack=[]
        curr_num=0
        operator="+"
        
        all_operators={"+","-","*","/"}
        
        for indx in range(len(s)):
            char=s[indx]
            
            if char.isdigit():
                curr_num=curr_num*10 + int(char)
            
            if char in all_operators or indx==len(s)-1:
                
                if operator=="+":
                    stack.append(curr_num)
                    
                elif operator=="-":
                    stack.append(-curr_num)
                    
                elif operator=="*":
                    stack[-1]*=curr_num
                    
                elif operator=="/":
                    stack[-1] = int(stack[-1]/curr_num)
                    
                curr_num=0
                operator=char
        
        return sum(stack)