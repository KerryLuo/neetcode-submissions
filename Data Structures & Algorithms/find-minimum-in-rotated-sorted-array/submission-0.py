# 1 6
# 3 5


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = int((l + r) / 2)

            
            print(l, r, m)

            if nums[m] > nums[r]:
                l = m + 1

            elif nums[m] < nums[r]:
                r = m

            else:
                return nums[m]
            
        return nums[int(min(l, r))]