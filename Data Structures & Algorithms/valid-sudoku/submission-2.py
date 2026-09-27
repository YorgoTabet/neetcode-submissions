class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxMap = [[set() for i in range(3)] for _ in range(3)]

        for row in range(9):
            rowSet = set()
            colSet = set()
            for col in range(9):
                rowEl = board[row][col]
                colEl = board[col][row]

                if rowEl in rowSet and rowEl != ".":
                    return False
                else:
                    rowSet.add(rowEl)

                if colEl in colSet and colEl != ".":
                    return False
                else:
                    colSet.add(colEl)

                if rowEl in boxMap[row // 3][col // 3] and rowEl != ".":
                    return False
                else:
                    boxMap[row // 3][col // 3].add(rowEl)

        return True
