class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        for string in strs:
            s = "".join(sorted(string))
            if s in anaDict:
                anaDict[s].append(string)
            else:
                anaDict[s] = [string]

        return list(anaDict.values())
        