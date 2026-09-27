class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxMap = [[[False] * 9 for i in range(3)] for _ in range(3)]

        for row in range(9):
            rowSet = [False] * 9
            colSet = [False] * 9
            for col in range(9):
                rowEl = board[row][col]
                colEl = board[col][row]

                if rowEl != ".":
                    if rowSet[int(rowEl) - 1]:
                        return False
                    else:
                        rowSet[int(rowEl) - 1] = True

                if colEl != ".":
                    if colSet[int(colEl) - 1]:
                        return False
                    else:
                        colSet[int(colEl) - 1] = True

                if rowEl != ".":
                    if boxMap[row // 3][col // 3][int(rowEl) - 1]:
                        return False
                    else:
                        boxMap[row // 3][col // 3][int(rowEl) - 1] = True

        return True
