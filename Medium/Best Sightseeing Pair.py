class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        maxValue2 = values[-1]-(len(values)-1)
        Value2 = maxValue2
        for i in range(len(values)-2, -1, -1):
            Value1 = values[i]+i
            if maxScore< Value1+maxValue2:
                maxScore = Value1+maxValue2
            
            Value2 = values[i]-i
            if maxValue2<Value2:
                maxValue2=Value2

        return maxScore