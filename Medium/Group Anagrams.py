class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict=collections.defaultdict(list)
        
        for i in strs:
            dict[tuple(sorted(i))].append(i)
            
        return dict.values()