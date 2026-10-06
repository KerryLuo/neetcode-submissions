# for each substring that you select, there will be a character that occurs the most that will be the main character, the rest of the characters will sum to k
# for each char in string, expand the window until you can't anymore (num chars other than maxNumChar sum to k)

from collections import defaultdict
# my_dict = defaultdict(int)
# sum(d.values()) - max(d.values())


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        d = defaultdict(int)

        # increment right
        for right in range(len(s)):
            d[s[right]] += 1

            # if sum of other char > k, incremement left
            while (right - left + 1) - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength

        
        






        return maxLength