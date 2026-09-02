class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        valid = "qwertyuiopasdfghjklzxcvbnm1234567890"

        while i <= j:
            while i < j and s[i].lower() not in valid:
                i += 1
            
            while i < j and s[j].lower() not in valid:
                j -= 1
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True