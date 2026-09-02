from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = deque()

        for p, s in pair:
            time = (target - p) / s
            
            if len(fleets) == 0:
                fleets.append(time)
            else:
                fleets.append(time)
                if fleets[-2] >= fleets[-1]:
                    fleets.pop()
        
        return len(fleets)


        