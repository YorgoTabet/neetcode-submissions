class Solution:
    def binarySearch(self, arr: List[int], target:int) -> bool:
        l,r = 0, len(arr) - 1

        while l <= r:
            mid = math.floor((r-l) / 2 + l)
            
            if(arr[mid] == target):
                return True
            if(target < arr[mid]):
                r = mid - 1
            else:
                l = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_length = len(matrix)
        n_length = len(matrix[0])
        
        for m in range(m_length):
            if( target >= matrix[m][0] and target <= matrix[m][n_length - 1]):
                return self.binarySearch(matrix[m], target)


        return False