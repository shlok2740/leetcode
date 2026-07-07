class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        str_num=str(n)
        length=len(str_num)
        result=sum(len(digits)**i for i in range(1,length))
        i=0
        while i < length:
            result+=sum(digit < str_num[i] for digit in digits) * (len(digits)**(length-i-1))
            if str_num[i] not in digits:
                break
            i+=1
        
        return result + (i==length)