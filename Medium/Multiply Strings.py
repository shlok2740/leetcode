class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        
        def decode(num):
            ans=0
            for i in num:
                ans = ans*10 + (ord(i)-ord('0'))
                
            return ans
        
        
        def encode(string):
            char=""
            
            while string:
                string1=string%10
                string=string//10
                
                char=chr(ord('0')+string1)+char
                
            return char
        
        
        return encode(decode(num1)*decode(num2))