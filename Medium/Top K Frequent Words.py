class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        
        for w in words:
            if w in dic:
                dic[w]+=1
            else:
                dic[w]=1
                
        res = sorted(dic.keys(),key=lambda x:(-dic[x],x))
        return res[:k]