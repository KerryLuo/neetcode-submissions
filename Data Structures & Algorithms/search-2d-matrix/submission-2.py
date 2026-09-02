# binary search rows until you get to a row[0] < target 
# and the next row[0] > target

# then regular binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c, r = len(matrix), len(matrix[0]) # row & col length

        left, right = 0, r * c - 1 # all elements

        while left <= right: 
            mid = (left + right) // 2

            row = mid // r
            col = mid % r

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return False





         


        