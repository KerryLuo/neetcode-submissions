from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = sorted(range(len(position)), key=lambda i: position[i])

        fleets = deque()

        for i in reversed(indices):
            time = (target - position[i]) / speed[i]
            
            if len(fleets) == 0:
                fleets.append(time)
            elif fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)


        