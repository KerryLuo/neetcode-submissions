class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for n in range(len(nums) + 1):
            result ^= n
        
        for n in nums:
            result ^= n
        
        return result