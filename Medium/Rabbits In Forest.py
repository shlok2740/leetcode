class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        count=collections.Counter()
        for i in answers:
            if count[i]%(i+1)==0:
                res+=i+1
            count[i]+=1
            
        return res