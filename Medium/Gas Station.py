class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas)==0 or len(cost)==0 or sum(gas)<sum(cost):
            return -1
        
        position = 0 
        fuel = 0
        
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel<0:
                fuel=0
                position=i+1
                
        return position