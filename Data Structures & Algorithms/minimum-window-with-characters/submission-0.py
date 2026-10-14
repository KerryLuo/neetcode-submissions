# variable length sliding window
# turn both into frequency tables
# check if t is in s (just need a num >= to t) --> if not, return false
# sliding window --> starting from left, increment right until satisfies, then increment y until you can't. Save substring. Then increment left one time --> repeat until possibly another substring works out

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, d = defaultdict(int), defaultdict(int)

        for char in t:
            target[char] += 1
        
        for char in s:
            d[char] += 1
        
        # is there a valid substring?
        for key in target.keys():
            if d[key] < target[key]:
                return ""
        
        # there is a valid substring
        left = 0
        satisfied = 0

        substring = defaultdict(int)
        minWindow = ""

        for right in range(len(s)):
            substring[s[right]] += 1
            if s[right] in target and substring[s[right]] == target[s[right]]:
                satisfied += 1

            while satisfied == len(target.keys()):
                if minWindow == "" or right - left + 1 < len(minWindow):
                    minWindow = s[left:right + 1]
                
                substring[s[left]] -= 1

                if s[left] in target and substring[s[left]] < target[s[left]]:
                    satisfied -= 1
                
                left += 1
        
        return minWindow

        

                
        