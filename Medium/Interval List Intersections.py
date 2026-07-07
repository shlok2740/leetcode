class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        firstList.extend(secondList)
        firstList.sort()
        
        res = []
        curr_r = firstList[0][1]
        
        for i in range(1,len(firstList)):
            
            if firstList[i][0]<=curr_r:
                
                res.append([firstList[i][0],min(curr_r,firstList[i][1])])
            
            curr_r = max(curr_r,firstList[i][1])
        
        return res