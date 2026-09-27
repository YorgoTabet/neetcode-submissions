class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ocSet = set()

        for row in range(9):
            ocSet.clear()
            for col in range(9):
                el = board[row][col]

                if el in ocSet and el != ".":
                    return False
                else:
                    ocSet.add(el)

        
        for col in range(9):
            ocSet.clear()
            for row in range(9):
                el = board[row][col]
                if el in ocSet and el != ".":
                    return False
                else:
                    ocSet.add(el)

        
        BOX_INDICIES = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

        for row in range(0, 9, 3):
            ocSet.clear()
            for col in range(0, 9, 3):
                ocSet.clear()
                for offset in BOX_INDICIES:
                    if (
                        board[row + offset[0]][col + offset[1]] in ocSet
                        and board[row + offset[0]][col + offset[1]] != "."
                    ):
                        return False
                    else:
                        ocSet.add(board[row + offset[0]][col + offset[1]])
        
        return True

