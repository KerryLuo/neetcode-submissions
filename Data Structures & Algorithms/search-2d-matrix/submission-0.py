# binary search rows until you get to a row[0] < target 
# and the next row[0] > target

# then regular binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1

        while bottom <= top:
            mid = (top + bottom) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                top = mid - 1
            else:
                bottom = mid + 1

        # the correct row is always top? 

        row = matrix[top]
        print(row, top)

        bottom, top = 0, len(row) - 1

        while bottom <= top:
            mid = (top + bottom) // 2
            print(bottom, top, mid)

            if row[mid] == target:
                return True
            elif row[mid] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        print("failed")
        return False




         


        