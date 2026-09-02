# two lists, one going right and another going left
# each one iterates through the height list and records the index of the greatest value

class Solution:
    def trap(self, height: List[int]) -> int:
        water = []
        leftGreatest = [0]
        rightGreatest = [len(height) - 1]

        for i in range(1, len(height)):
            if height[i] >= height[leftGreatest[-1]]:
                leftGreatest.append(i)
            else:
                leftGreatest.append(leftGreatest[-1])

        for i in reversed(range(len(height) - 1)):
            if height[i] >= height[rightGreatest[-1]]:
                rightGreatest.append(i)
            else:
                rightGreatest.append(rightGreatest[-1])
        rightGreatest = rightGreatest[::-1]
        
        # now we have the lists that store the index of the greatest value to the left/right of any given index

        def calculateWater(num, i, j):
            return min(height[i], height[j]) - height[num]
        
        for i in range(len(height)):
            if i == leftGreatest[i] or i == rightGreatest[i]:
                water.append(0)
                pass
            else:
                water.append(calculateWater(i, leftGreatest[i], rightGreatest[i]))

        return sum(water)
