class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        actual_sum = 0
        exp_sum = 0

        # Sum of elements present in array
        for i in range(l):
            actual_sum += nums[i]

        # Expected sum from 0 to l
        for i in range(l + 1):
            exp_sum += i

        # Missing number = expected - actual
        return exp_sum - actual_sum