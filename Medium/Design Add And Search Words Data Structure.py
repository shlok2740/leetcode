class WordDictionary:

    def __init__(self):
        self.words = '#'
    
    def addWord(self, word):
        self.words += word + '#'

    def search(self, word):
        return bool(re.search('#' + word + '#', self.words))
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)