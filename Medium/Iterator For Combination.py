class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combos=[]
        self.indx=0
        
        def helper(string,indx):
            if len(string)==combinationLength:
                self.combos.append(string)
                return
            else:
                for i in range(indx,len(characters)):
                    helper(string+characters[i],i+1)
                    
        helper("",0)

    def next(self) -> str:
        self.indx+=1
        return self.combos[self.indx-1]

    def hasNext(self) -> bool:
        return self.indx<len(self.combos)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()