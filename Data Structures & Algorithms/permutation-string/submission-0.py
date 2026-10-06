# this is fixed length sliding window

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        
        if length > len(s2):
            return False
        
        # preprocess s1 --> d1 = letter:freq
        target = defaultdict(int)
        for i in range(length):
            target[s1[i]] += 1

        # begin iteration
        d = defaultdict(int)

        for left in range(len(s2) - length + 1):
            right = left + length - 1

            # construct dict at beginning
            if left == 0:
                for i in range(length):
                    d[s2[i]] += 1
            else:
                d[s2[left - 1]] -= 1
                if d[s2[left - 1]] == 0:
                    del d[s2[left - 1]]
                d[s2[right]] += 1
            
            if d == target:
                return True

        return False

