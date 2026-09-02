class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}

        for item in nums:
            if item in numDict:
                numDict[item] += 1
            else:
                numDict[item] = 1
        
        # we now have a dictionary where (nums as set) : (occurences)
        # now use bucket sort on numDict

        # bucket is # of occurences : nums

        buckets = [[] for _ in range(len(nums) + 1)]

        for item in numDict:
            buckets[numDict[item]].append(item)

        final = []

        for i in range(len(nums), 0, -1):
            for item in buckets[i]:
                final.append(item)
                if len(final) == k:
                    return final








        # sorted_dict = dict(sorted(numDict.items(), key=lambda item: item[1]))
        # return sorted(sorted_dict, key=sorted_dict.get, reverse=True)[:k]



# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         buckets = {i: [] for i in range(len(nums) + 1)}

#         x = set(nums)

#         for num in x:
#             freq = nums.count(num)

#             buckets[freq].append(num)
        
#         final = [item for i in range(len(nums) + 1) for item in buckets[i]]

#         return final[-k:]


        