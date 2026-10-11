class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])


        l = 0
        r = ROWS * COLS - 1

        while(l <= r):
            mid = l + (r - l) // 2

            midM = mid // COLS
            midN = mid % COLS

            print(midM, midN)
            if(matrix[midM][midN] == target):
                return True
            
            if(target < matrix[midM][midN]):
                r = mid - 1
            else:
                l = mid + 1

        return False
