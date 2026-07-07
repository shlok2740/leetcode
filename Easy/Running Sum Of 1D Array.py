class Solution:
    def runningSum(self, nums):
        sums=0
        runSum=[]
        for i in range(len(nums)):
             sums+=nums[i]
             runSum.append(sums)
        return runSum
    