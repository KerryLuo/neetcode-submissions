# set nums[i]
# for j and k, solve as regular 2sum problem. If greater/lesser, change k/j

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid = []

        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    valid.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                    k -= 1

                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                elif total > 0:                    
                    k -= 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                else:
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        
        return valid

