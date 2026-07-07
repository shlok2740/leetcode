class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_cnt,even_cnt=0,0
        for i in range(len(position)):
            if position[i]%2==1:
                odd_cnt+=1
            else:
                even_cnt+=1
                
        return odd_cnt if odd_cnt<even_cnt else even_cnt