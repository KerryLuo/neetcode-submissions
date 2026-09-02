class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        prefix = []
        postfix = []

        rev = nums[::-1]

        i = 0

        pre = 1
        post = 1

        while i < len(nums):
            prefix.append(pre)
            postfix.append(post)
            
            pre *= nums[i]
            post *= rev[i]
            
            i += 1

        # now we have a prefix and postfix, postfix is done so that 0 to x is the last x of the nums list

        final = []

        for i in range(len(nums)):
            final.append(prefix[i] * postfix[len(nums) - i - 1])
        
        return final


