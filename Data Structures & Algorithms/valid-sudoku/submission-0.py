class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]

        def findSquare(row, col):
            return (row // 3) * 3 + (col // 3)

        # i is row
        # j is column

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                elif item in rows[i] or item in cols[j] or item in squares[findSquare(i, j)]:
                    return False
                else:
                    rows[i].append(item)
                    cols[j].append(item)
                    squares[findSquare(i, j)].append(item)
        return True
                
                



