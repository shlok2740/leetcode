class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)
        
        def repLace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word
        
        return " ".join(map(repLace, sentence.split()))