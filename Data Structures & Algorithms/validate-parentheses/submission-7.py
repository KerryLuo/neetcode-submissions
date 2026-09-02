from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        temp = deque()

        for char in s:
            if char not in lookup:
                temp.append(char)
            elif not temp:
                return False
            else:
                if temp[-1] == lookup[char]:
                    temp.pop()
                else:
                    return False
        
        if not temp:
            return True
        else:
            return False



        