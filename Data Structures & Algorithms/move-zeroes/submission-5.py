class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t1 = []
        t2 = []

        for i in range(len(nums)):
            if nums[i] != 0:
                t1.append(nums[i])
            else:
                t2.append(nums[i])
        nums.clear()
        nums.extend(t1+t2)         