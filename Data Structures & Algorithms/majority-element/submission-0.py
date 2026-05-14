class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        limit = n // 2

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1   # important: += 1
                if count > limit:
                    return nums[i]
        