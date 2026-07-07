class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        # Step 2: Sort by repeated string
        nums.sort(key=lambda x: x*10, reverse=True)

        # Step 3: Concatenate
        result = "".join(nums)

        # Step 4: Handle leading zeros
        return str(int(result))
        