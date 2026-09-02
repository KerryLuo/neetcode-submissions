class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = sorted(range(len(position)), key=lambda i: position[i])

        slowest = None
        fleets = 0

        for i in reversed(indices):
            time = (target - position[i]) / speed[i]
            
            if slowest == None:
                slowest = time
                fleets += 1
            elif slowest < time:
                fleets += 1
                slowest = time
        
        return fleets


        