class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)

        info = {}
    
        def chain(n):
            start = n

            if n in info:
                return info[n]

            steps = 0 # number of steps you take from num -> num

            while n + 1 in lookup and n + 1 not in info:
                # iterate until you find the last item in the chain
                 steps += 1
                 n += 1
            # you now have largest n and num of steps
            # from 1 to 5 you took 4 steps and n is 5
            if n + 1 in info:
                increment = info[n + 1]
            else: 
                increment = 0

            info[n] = 1 + increment

            for step in range(steps):
                info[n - step - 1] = step + 2 + increment
            
            return info[start]


        m = 0
        
        for n in nums:
            if n not in info:
                temp = chain(n)
                if temp > m:
                    m = temp
            else:
                pass
        
        return m
        

        