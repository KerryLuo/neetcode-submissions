class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = int((l + r) / 2)
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        # index of min number
        minimum = int(r)

        # find the half the target could be in, min index included
        if nums[-1] > target:
            left, right = minimum, len(nums) -1
        elif nums[-1] < target:
            left, right = 0, minimum
        else:
            return len(nums) - 1
        
        # binary search to find if target is in bounds, exits if not found
        while left < right:
            m = int((left + right) / 2)

            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m
        
        if nums[left] == target:
            return left

        return -1