# start at the ends of the list and whichever of the two is shorter, increment that by 1 and check if new area is bigger, repeat until i > j

#came to me in a dream bro wtfff

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        mostWater = 0

        while i < j:
            height = min(heights[i], heights[j])
            width = j - i

            mostWater = max(mostWater, height * width)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return mostWater
        