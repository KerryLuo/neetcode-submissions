class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        maxFreq = 0
        d = defaultdict(int)

        for right in range(len(s)):
            d[s[right]] += 1
            maxFreq = max(maxFreq, d[s[right]])

            while (right - left + 1) - maxFreq > k:
                d[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength