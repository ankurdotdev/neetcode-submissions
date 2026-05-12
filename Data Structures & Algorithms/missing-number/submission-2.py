class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        freq = {}
        for i in range(0, l+1):
            freq[i] = 0

        for i in  range(l):
            freq[nums[i]] = 1

        for k,v in freq.items():
            if v == 0:
                return k    
