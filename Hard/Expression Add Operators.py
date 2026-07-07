class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def cal(nums, express, pre_num, cur_ans):
            n = len(nums)
            if n == 0:
                if cur_ans == target:
                    res.append(express)
                return
            for i in range(1, n+1):
                if i > 1 and nums[0] == '0':
                    break
                cur_num = int(nums[:i])
                if express == '':
                    cal(nums[i:], nums[:i], cur_num, cur_num)
                else:
                    if int(nums) >= abs(cur_ans - target):
                        cal(nums[i:], express+'+'+nums[:i], cur_num, cur_ans+cur_num)
                        cal(nums[i:], express+'-'+nums[:i], -cur_num, cur_ans-cur_num)
                    cal(nums[i:], express+'*'+nums[:i], pre_num*cur_num, cur_ans-pre_num+pre_num*cur_num)
            
        res = []
        cal(num, '', 0, 0)
        return res