class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        temp = []

        for char in s:
            if char not in lookup:
                temp.append(char)
            elif temp == []:
                return False
            else:
                if temp[-1] == lookup[char]:
                    temp.pop()
                else:
                    return False
        
        if temp == []:
            return True
        else:
            return False



        