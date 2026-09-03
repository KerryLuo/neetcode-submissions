# binary search from 1 to time // max pile value * pile num (extra)

# binary search from 1 to max pile value
# create a function that returns the total num of hours given k
# higher/lower by binary search of k

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            hours = 0

            for pile in piles:
                hours += int(-(-pile // k))

            return hours
        
        left, right = 1, max(piles)

        k = None
        
        while left <= right:
            mid = (left + right) // 2 # values for k

            if eat(mid) <= h:
                if k != None:
                    k = min(k, mid)
                else:
                    k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return k
            
        