class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result  = len(nums)
        for n in range(len(nums)):
            result ^= n ^ nums[n]
        return result